-- # Class: CisControls Description: One edition of the CIS Controls as a whole: its Controls, each holding its Safeguards.
--     * Slot: id
--     * Slot: cis_version Description: The edition, as CIS numbers it, such as 8.1, or the revision the guide's pages carry, such as 8.1.2.
-- # Class: CisControl Description: One of the CIS Controls: a group of Safeguards on one subject, named by its number, such as Control 4.
--     * Slot: id
--     * Slot: cis_control_id Description: The Control's identifier, its number, such as 4.
--     * Slot: title Description: A name for the Control or Safeguard, in words its user has the right to use.
--     * Slot: description Description: What the Control or Safeguard means to its user, in words its user has the right to use.
--     * Slot: CisControls_id Description: Autocreated FK slot
-- # Class: CisSafeguard Description: One Safeguard of a Control: a single action an enterprise takes, named by its Control's number and its own, such as Safeguard 4.1.
--     * Slot: id
--     * Slot: cis_safeguard_id Description: The Safeguard's identifier, its number, such as 4.1.
--     * Slot: title Description: A name for the Control or Safeguard, in words its user has the right to use.
--     * Slot: description Description: What the Control or Safeguard means to its user, in words its user has the right to use.
--     * Slot: safeguard_asset_class Description: The class of enterprise asset the Safeguard is about.
--     * Slot: safeguard_security_function Description: The security function the Safeguard serves, one of the six functions of the NIST Cybersecurity Framework (CSF) 2.0.
--     * Slot: CisControl_id Description: Autocreated FK slot
-- # Class: CisSafeguard_safeguard_implementation_groups
--     * Slot: CisSafeguard_id Description: Autocreated FK slot
--     * Slot: safeguard_implementation_groups Description: The Implementation Groups that include the Safeguard.

CREATE TABLE "CisControls" (
	id INTEGER NOT NULL,
	cis_version TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_CisControls_id" ON "CisControls" (id);

CREATE TABLE "CisControl" (
	id INTEGER NOT NULL,
	cis_control_id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	"CisControls_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CisControls_id") REFERENCES "CisControls" (id)
);
CREATE INDEX "ix_CisControl_id" ON "CisControl" (id);

CREATE TABLE "CisSafeguard" (
	id INTEGER NOT NULL,
	cis_safeguard_id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	safeguard_asset_class VARCHAR(13) NOT NULL,
	safeguard_security_function VARCHAR(8) NOT NULL,
	"CisControl_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CisControl_id") REFERENCES "CisControl" (id)
);
CREATE INDEX "ix_CisSafeguard_id" ON "CisSafeguard" (id);

CREATE TABLE "CisSafeguard_safeguard_implementation_groups" (
	"CisSafeguard_id" INTEGER,
	safeguard_implementation_groups VARCHAR(3) NOT NULL,
	PRIMARY KEY ("CisSafeguard_id", safeguard_implementation_groups),
	FOREIGN KEY("CisSafeguard_id") REFERENCES "CisSafeguard" (id)
);
CREATE INDEX "ix_CisSafeguard_safeguard_implementation_groups_CisSafeguard_id" ON "CisSafeguard_safeguard_implementation_groups" ("CisSafeguard_id");
CREATE INDEX "ix_CisSafeguard_safeguard_implementation_groups_safeguard_implementation_groups" ON "CisSafeguard_safeguard_implementation_groups" (safeguard_implementation_groups);
