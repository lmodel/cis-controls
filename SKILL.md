---
name: linkml-schema
description: "Author and evolve LinkML schemas in YAML. Use when: authoring schema classes, slots, enums, or types; mapping a source document (spec, PDF, standard) to a LinkML schema; adding new entities from a domain model; checking schema conventions; running gen-project, lint, or test recipes."
argument-hint: "What do you want to model or which source document are you mapping?"
---

# LinkML Schema Authoring

Schema: `src/<schema_name>/schema/<schema_name>.yaml`

```yaml
id: https://w3id.org/lmodel/<schema-name>
name: <schema-name>
description: |- One-line description
license: Apache-2.0
see_also: [https://example.org/spec]
prefixes:
  <schema_name>: https://w3id.org/lmodel/<schema-name>/
  linkml: https://w3id.org/linkml/
  schema: http://schema.org/
  dct: http://purl.org/dc/terms/
default_prefix: <schema_name>
default_range: string
imports:
  - linkml:types
  # - ./other_module   # modular split
types: {}
subsets: {}
enums: {}
slots: {}
classes: {}
```

---

## Prefixes Reference

Add only prefixes used in `slot_uri`, `meaning`, or `*_mappings`.

```yaml
prefixes:
  # core semantic web
  rdf:       http://www.w3.org/1999/02/22-rdf-syntax-ns#
  rdfs:      http://www.w3.org/2000/01/rdf-schema#
  xsd:       http://www.w3.org/2001/XMLSchema#
  owl:       http://www.w3.org/2002/07/owl#
  skos:      http://www.w3.org/2004/02/skos/core#
  # FAIR backbone
  schema:    http://schema.org/
  dct:       http://purl.org/dc/terms/
  dcat:      http://www.w3.org/ns/dcat#
  prov:      http://www.w3.org/ns/prov#
  foaf:      http://xmlns.com/foaf/0.1/
  void:      http://rdfs.org/ns/void#
  # encyclopedic
  WIKIDATA:          https://www.wikidata.org/wiki/
  WIKIDATA_PROPERTY: https://www.wikidata.org/prop/
  # OBO foundry
  BFO:   http://purl.obolibrary.org/obo/BFO_
  IAO:   http://purl.obolibrary.org/obo/IAO_
  RO:    http://purl.obolibrary.org/obo/RO_
  PATO:  http://purl.obolibrary.org/obo/PATO_
  # technology / CS domain
  cso:    https://cso.kmi.open.ac.uk/topics/
  opencs: https://w3id.org/opencs/
  SWO:    http://www.ebi.ac.uk/swo/
  EDAM:   http://edamontology.org/
  SAREF:  https://saref.etsi.org/core/
  ACM:    https://dl.acm.org/pb-assets/dl_ccs/
  # cybersecurity / lmodel
  iso27001:   https://lmodel.github.io/iso27001/
  nist800_53: https://lmodel.github.io/nist-sp-800-53/
  oscal:      https://lmodel.github.io/oscal/
  d3fend:     https://lmodel.github.io/d3fend/
  attack:     https://lmodel.github.io/attack/
  capec:      https://lmodel.github.io/capec/
  stix:       https://lmodel.github.io/stix/
  slsa:       https://lmodel.github.io/slsa/
  spdx:       https://lmodel.github.io/spdx/
  nist_csf:   https://lmodel.github.io/nist-csf-v2/
  uco:        https://lmodel.github.io/uco-core/
  # identifiers
  ORCID:       https://orcid.org/
  doi:         https://doi.org/
  bioregistry: https://bioregistry.io/
```

---

## Authoring Checklist

### Subsets (`name` snake_case) / Types (custom scalars only)
```yaml
subsets:
  core_controls: {description: Foundational controls.}
types:
  ControlId: {uri: xsd:string, base: str, pattern: "^CIS-[0-9]+\\.[0-9]+$"}
```

### Enumerations
`name` PascalCase; values snake_case; `description` on each value (omit if self-evident); `meaning` for ontology URI.

```yaml
enums:
  ImplementationGroup:                    # static — hand-maintained
    description: Tier of control applicability
    permissible_values:
      IG1: {description: Basic cyber hygiene}
      IG2: {description: For organizations managing sensitive data}
      IG3: {description: For high-risk profiles, meaning: CIS:IG3}

  DiseaseTerms:                           # dynamic — re-syncs from ontology at build
    reachable_from:
      source_ontology: bioregistry:mondo
      source_nodes: [MONDO:0000001]
      relationship_types: [rdfs:subClassOf]
      include_self: false
  # ⚠ linkml validate / gen-json-schema don't resolve reachable_from at runtime.
  # Materialize first: vskit expand -s schema.yaml -o schema_expanded.yaml

  ExtendedIG:                             # composition: inherit + extend
    inherits: [ImplementationGroup]
    permissible_values:
      IG0: {description: Experimental tier}

  CoreTiersOnly:                          # composition: subtract
    inherits: [ImplementationGroup]
    minus:
      - permissible_values: {IG3: {}}
```

### Slots — always schema-level; `slot_usage` for per-class overrides
- `name` snake_case; `range` explicit; `multivalued: true` for lists; `inlined_as_list: true` for object lists
- `required: true` only for mandatory fields; `slot_uri` maps to RDF property
- `domain` restricts to a class; `aliases` for alternate names
- `inverse` on both directions; `symmetric`/`transitive`/`reflexive` for predicate semantics
- `any_of: [{range: MyEnum}, {range: string}]` for open-range; `values_from` for CURIE-namespace open vocab
- `deprecated: true` + `deprecated_element_has_exact_replacement` when retiring

```yaml
slots:
  id:
    identifier: true
    range: string
    required: true
    exact_mappings: [schema:identifier, dct:identifier]
  title:
    range: string
    required: true
    slot_uri: dct:title
  name:
    aliases: ['label', 'display name']
    slot_uri: rdfs:label
    range: string
  causes:
    range: named_thing
    inverse: caused_by
    transitive: true
  caused_by:
    range: named_thing
    inverse: causes
  topic:
    any_of:
      - range: TopicEnum   # curated
      - range: string      # escape hatch
  category:
    slot_uri: rdf:type
    multivalued: true
    values_from: [MyOntologyNamespace]
```

### Classes
- `name` PascalCase; `abstract: true` = base (no instantiation); `mixin: true` = cross-cutting (no `is_a`)
- `is_a` for subtypes; `mixins` list for shared behavior; `tree_root: true` on root container
- `id_prefixes` declares valid CURIE namespaces for instances (used by validators)
- `*_mappings`, `see_also`, `aliases`, `annotations`, `notes`, `comments` for documentation and alignment

```yaml
classes:
  OntologyBacked:        # mixin
    mixin: true
    slots: [id]

  NamedThing:            # abstract base
    abstract: true
    slots: [id, title]
    exact_mappings: [BFO:0000001]

  SecurityControl:
    is_a: NamedThing
    mixins: [OntologyBacked]
    tree_root: true
    slots: [implementation_groups]
    slot_usage:
      description: {description: Description specific to a SecurityControl.}
    aliases: ['safeguard', 'control']
    id_prefixes: [CIS]
    exact_mappings: [schema:Action, WIKIDATA:Q2695280]
    narrow_mappings: [NCIT:C94273]
    see_also: [https://www.cisecurity.org/controls/]
    in_subset: [core_controls]
```

---

## Source Document → Schema Mapping

| Source element | Schema target |
|---|---|
| Persistent noun | `class` |
| Controlled-list noun | `enum` |
| Property / attribute | schema-level `slot` |
| Verb / relationship | `slot` with object `range` + `inverse` |
| Containment root | class with `tree_root: true` |
| Inheritance | `is_a:` chain |
| Shared cross-type behavior | `mixin:` |
| External code / URI | `meaning:` on enum value or `*_mappings:` on class/slot |

Checklist: every class has `identifier`; enum values have `meaning:`; `is_a` matches hierarchy; `id_prefixes` set when CURIEs are known.

---

## Ontology Alignment

| Key | Applies to | Meaning | RDF/OWL equivalent |
|---|---|---|---|
| `exact_mappings` | class, slot, enum | 1:1 equivalence | `owl:equivalentClass` / `owl:equivalentProperty` |
| `close_mappings` | class, slot | Substantially similar | `skos:closeMatch` |
| `narrow_mappings` | class, slot | Schema term more specific | `skos:narrowMatch` |
| `broad_mappings` | class, slot | Schema term more general | `skos:broadMatch` |
| `related_mappings` | class, slot | Related, no precise fit | `skos:relatedMatch` |
| `slot_uri` | slot | Maps to RDF property URI | used directly as predicate in triples |
| `id_prefixes` | class | Valid CURIE namespaces for instances | — |
| `values_from` | slot | Open-vocab CURIE namespace | — |
| `meaning` | enum value | Ontology term URI for a value | `owl:sameAs` |

Stack mappings across vocabularies for max KG interoperability:
`exact_mappings: [schema:Action, WIKIDATA:Q2695280, NCIT:C94273]`

---

## Commands & Quality Gates

| Goal | Command |
|---|---|
| Validate schema | `just lint` |
| Regenerate all artifacts | `just gen-project` |
| Regenerate docs | `just gen-doc` |
| Run tests | `just test` |
| Local doc preview | `just testdoc` |

Gate: `just lint` → `just gen-project` → `just test` after every schema edit.  
Test data: `tests/data/valid/<ClassName>-<desc>.yaml` / `invalid/` — stem prefix must match class name.
