-- # Class: CISControlsDocument Description: Root container for a versioned edition of the CIS Critical Security Controls publication.
--     * Slot: id Description: Unique identifier for the element.
--     * Slot: title Description: Human-readable title of the element.
--     * Slot: description Description: Descriptive text for the element.
--     * Slot: version Description: Version string of the CIS Controls document (e.g. "8.1").
--     * Slot: publication_date Description: Publication date of the CIS Controls document (ISO 8601).
-- # Class: CISControl Description: One of the CIS Critical Security Controls; a high-level defensive action category that enterprises should implement to reduce cyber risk.
--     * Slot: id Description: Composite identifier for the control (e.g. "CIS-1").
--     * Slot: title Description: Human-readable title of the element.
--     * Slot: control_number Description: Numeric identifier of the parent CIS Control (1–18).
--     * Slot: overview Description: Brief description of the intent of a Control and its utility as a defensive action.
--     * Slot: why_critical Description: Explanation of the importance of this Control in blocking, mitigating, or identifying attacks, and how attackers exploit its absence.
--     * Slot: procedures_and_tools Description: Technical description of the processes and technologies that enable implementation and automation of this Control.
--     * Slot: CISControlsDocument_id Description: Autocreated FK slot
-- # Class: Safeguard Description: A specific, measurable action that an enterprise should take to implement a CIS Control. Formerly called "Sub-Controls" prior to CIS Controls v8.
--     * Slot: id Description: Composite identifier for the safeguard (e.g. "CIS-1.1").
--     * Slot: title Description: Human-readable title of the element.
--     * Slot: safeguard_number Description: Dotted identifier of this Safeguard (e.g. "1.1"). Combines the parent control number with a sequential Safeguard index.
--     * Slot: description Description: Descriptive text for the element.
--     * Slot: asset_type Description: The class of enterprise asset primarily addressed by this Safeguard.
--     * Slot: security_function Description: NIST CSF 2.0 function category to which this Safeguard is mapped.
--     * Slot: CISControl_id Description: Autocreated FK slot
-- # Class: Safeguard_implementation_groups
--     * Slot: Safeguard_id Description: Autocreated FK slot
--     * Slot: implementation_groups Description: Implementation Group(s) for which this Safeguard is applicable. A Safeguard listed under IG2 is also required for IG3 enterprises; a Safeguard listed under IG1 is required for all enterprises.

CREATE TABLE "CISControlsDocument" (
	id TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	version TEXT,
	publication_date TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_CISControlsDocument_id" ON "CISControlsDocument" (id);

CREATE TABLE "CISControl" (
	id TEXT NOT NULL,
	title TEXT NOT NULL,
	control_number TEXT NOT NULL,
	overview TEXT,
	why_critical TEXT,
	procedures_and_tools TEXT,
	"CISControlsDocument_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("CISControlsDocument_id") REFERENCES "CISControlsDocument" (id)
);
CREATE INDEX "ix_CISControl_id" ON "CISControl" (id);

CREATE TABLE "Safeguard" (
	id TEXT NOT NULL,
	title TEXT NOT NULL,
	safeguard_number TEXT NOT NULL,
	description TEXT,
	asset_type VARCHAR(13) NOT NULL,
	security_function VARCHAR(8) NOT NULL,
	"CISControl_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("CISControl_id") REFERENCES "CISControl" (id)
);
CREATE INDEX "ix_Safeguard_id" ON "Safeguard" (id);

CREATE TABLE "Safeguard_implementation_groups" (
	"Safeguard_id" TEXT,
	implementation_groups VARCHAR(3) NOT NULL,
	PRIMARY KEY ("Safeguard_id", implementation_groups),
	FOREIGN KEY("Safeguard_id") REFERENCES "Safeguard" (id)
);
CREATE INDEX "ix_Safeguard_implementation_groups_Safeguard_id" ON "Safeguard_implementation_groups" ("Safeguard_id");
CREATE INDEX "ix_Safeguard_implementation_groups_implementation_groups" ON "Safeguard_implementation_groups" (implementation_groups);
