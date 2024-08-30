-- # Class: "PodProvider" Description: "General information about a pod provider"
--     * Slot: area Description: A human-readable location string of a Pod Provider.
--     * Slot: baseUrl Description: The base URL of a Pod Provider.
--     * Slot: providedBy Description: The instance name of the Pod Provider
-- # Class: "ClassDescription" Description: "Description of an RDFS class used in Type Registration"
--     * Slot: id Description: 
--     * Slot: icon Description: The icon to show for a resource's class.
--     * Slot: openEndpoint Description: 
--     * Slot: labelPredicate Description: The predicate used as a human-readable label for resources of a given class
--     * Slot: describedClass Description: The class described by a ClassDescription
--     * Slot: describedBy Description: The app registering a given ClassDescription.
--     * Slot: prefLabel Description: 
-- # Class: "Install" Description: "Activity to Install an app using Solid Application Interoperability"
--     * Slot: id Description: 
-- # Class: "Notification" Description: "A notification activity from an app to notify the user."
--     * Slot: id Description: 
-- # Class: "EventFormat" Description: ""
--     * Slot: id Description: 
--     * Slot: label Description: 
-- # Class: "Activity" Description: ""
--     * Slot: id Description: 
-- # Class: "Collection" Description: ""
--     * Slot: id Description: 
-- # Class: "OrderedCollection" Description: ""
--     * Slot: id Description: 
-- # Class: "PodProvider_locales" Description: ""
--     * Slot: PodProvider_baseUrl Description: Autocreated FK slot
--     * Slot: locales Description: A set of supported locale language tags of a Pod Provider.
-- # Class: "Install_acceptedAccessNeeds" Description: ""
--     * Slot: Install_id Description: Autocreated FK slot
--     * Slot: acceptedAccessNeeds Description: The access needs accepted in an app registration.
-- # Class: "Install_acceptedSpecialRights" Description: ""
--     * Slot: Install_id Description: Autocreated FK slot
--     * Slot: acceptedSpecialRights Description: The special access needs accepted in an app registration.

CREATE TABLE "PodProvider" (
	area TEXT, 
	"baseUrl" TEXT NOT NULL, 
	"providedBy" TEXT, 
	PRIMARY KEY ("baseUrl")
);
CREATE TABLE "ClassDescription" (
	id INTEGER NOT NULL, 
	icon TEXT, 
	"openEndpoint" TEXT, 
	"labelPredicate" TEXT, 
	"describedClass" TEXT, 
	"describedBy" TEXT, 
	"prefLabel" TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Install" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Notification" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "EventFormat" (
	id INTEGER NOT NULL, 
	label TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Activity" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Collection" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "OrderedCollection" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "PodProvider_locales" (
	"PodProvider_baseUrl" TEXT, 
	locales TEXT, 
	PRIMARY KEY ("PodProvider_baseUrl", locales), 
	FOREIGN KEY("PodProvider_baseUrl") REFERENCES "PodProvider" ("baseUrl")
);
CREATE TABLE "Install_acceptedAccessNeeds" (
	"Install_id" INTEGER, 
	"acceptedAccessNeeds" VARCHAR(19), 
	PRIMARY KEY ("Install_id", "acceptedAccessNeeds"), 
	FOREIGN KEY("Install_id") REFERENCES "Install" (id)
);
CREATE TABLE "Install_acceptedSpecialRights" (
	"Install_id" INTEGER, 
	"acceptedSpecialRights" VARCHAR(19), 
	PRIMARY KEY ("Install_id", "acceptedSpecialRights"), 
	FOREIGN KEY("Install_id") REFERENCES "Install" (id)
);