# Auto generated from activitypods-ontology.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-08-30T17:32:22
# Schema: activitypods-ontology
#
# id: http://activitypods.org/ns/core#
# description: LinkML ontology for ActivityPods
# license: Apache Software License 2.0

import dataclasses
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from datetime import date, datetime, time
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Boolean, Datetime, Integer, String, Uri, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URI, URIorCURIE, XSDDateTime

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
APODS = CurieNamespace('apods', 'https://activitypods.org/ns/core#')
AS = CurieNamespace('as', 'https://www.w3.org/ns/activitystreams#')
INTEROP = CurieNamespace('interop', 'https://www.w3.org/ns/solid/interop#')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
DEFAULT_ = APODS


# Types

# Class references
class PodProviderBaseUrl(URI):
    pass


@dataclass(repr=False)
class PodProvider(YAMLRoot):
    """
    General information about a pod provider
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = APODS["PodProvider"]
    class_class_curie: ClassVar[str] = "apods:PodProvider"
    class_name: ClassVar[str] = "PodProvider"
    class_model_uri: ClassVar[URIRef] = APODS.PodProvider

    baseUrl: Union[str, PodProviderBaseUrl] = None
    area: Optional[str] = None
    locales: Optional[Union[str, List[str]]] = empty_list()
    providedBy: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.baseUrl):
            self.MissingRequiredField("baseUrl")
        if not isinstance(self.baseUrl, PodProviderBaseUrl):
            self.baseUrl = PodProviderBaseUrl(self.baseUrl)

        if self.area is not None and not isinstance(self.area, str):
            self.area = str(self.area)

        if not isinstance(self.locales, list):
            self.locales = [self.locales] if self.locales is not None else []
        self.locales = [v if isinstance(v, str) else str(v) for v in self.locales]

        if self.providedBy is not None and not isinstance(self.providedBy, str):
            self.providedBy = str(self.providedBy)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ClassDescription(YAMLRoot):
    """
    Description of an RDFS class used in Type Registration
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = APODS["ClassDescription"]
    class_class_curie: ClassVar[str] = "apods:ClassDescription"
    class_name: ClassVar[str] = "ClassDescription"
    class_model_uri: ClassVar[URIRef] = APODS.ClassDescription

    icon: Optional[Union[str, URI]] = None
    openEndpoint: Optional[Union[str, URI]] = None
    labelPredicate: Optional[Union[str, URIorCURIE]] = None
    describedClass: Optional[Union[str, URIorCURIE]] = None
    describedBy: Optional[Union[str, URIorCURIE]] = None
    prefLabel: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.icon is not None and not isinstance(self.icon, URI):
            self.icon = URI(self.icon)

        if self.openEndpoint is not None and not isinstance(self.openEndpoint, URI):
            self.openEndpoint = URI(self.openEndpoint)

        if self.labelPredicate is not None and not isinstance(self.labelPredicate, URIorCURIE):
            self.labelPredicate = URIorCURIE(self.labelPredicate)

        if self.describedClass is not None and not isinstance(self.describedClass, URIorCURIE):
            self.describedClass = URIorCURIE(self.describedClass)

        if self.describedBy is not None and not isinstance(self.describedBy, URIorCURIE):
            self.describedBy = URIorCURIE(self.describedBy)

        if self.prefLabel is not None and not isinstance(self.prefLabel, URIorCURIE):
            self.prefLabel = URIorCURIE(self.prefLabel)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EventFormat(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = APODS["EventFormat"]
    class_class_curie: ClassVar[str] = "apods:EventFormat"
    class_name: ClassVar[str] = "EventFormat"
    class_model_uri: ClassVar[URIRef] = APODS.EventFormat

    label: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.label is not None and not isinstance(self.label, URIorCURIE):
            self.label = URIorCURIE(self.label)

        super().__post_init__(**kwargs)


class Activity(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AS["Activity"]
    class_class_curie: ClassVar[str] = "as:Activity"
    class_name: ClassVar[str] = "Activity"
    class_model_uri: ClassVar[URIRef] = APODS.Activity


@dataclass(repr=False)
class Install(Activity):
    """
    Activity to Install an app using Solid Application Interoperability
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = APODS["Install"]
    class_class_curie: ClassVar[str] = "apods:Install"
    class_name: ClassVar[str] = "Install"
    class_model_uri: ClassVar[URIRef] = APODS.Install

    acceptedAccessNeeds: Optional[Union[Union[str, "AccessNeed"], List[Union[str, "AccessNeed"]]]] = empty_list()
    acceptedSpecialRights: Optional[Union[Union[str, "AccessNeed"], List[Union[str, "AccessNeed"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.acceptedAccessNeeds, list):
            self.acceptedAccessNeeds = [self.acceptedAccessNeeds] if self.acceptedAccessNeeds is not None else []
        self.acceptedAccessNeeds = [v if isinstance(v, AccessNeed) else AccessNeed(v) for v in self.acceptedAccessNeeds]

        if not isinstance(self.acceptedSpecialRights, list):
            self.acceptedSpecialRights = [self.acceptedSpecialRights] if self.acceptedSpecialRights is not None else []
        self.acceptedSpecialRights = [v if isinstance(v, AccessNeed) else AccessNeed(v) for v in self.acceptedSpecialRights]

        super().__post_init__(**kwargs)


class Notification(Activity):
    """
    A notification activity from an app to notify the user.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = APODS["Notification"]
    class_class_curie: ClassVar[str] = "apods:Notification"
    class_name: ClassVar[str] = "Notification"
    class_model_uri: ClassVar[URIRef] = APODS.Notification


class Collection(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AS["Collection"]
    class_class_curie: ClassVar[str] = "as:Collection"
    class_name: ClassVar[str] = "Collection"
    class_model_uri: ClassVar[URIRef] = APODS.Collection


class OrderedCollection(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = AS["OrderedCollection"]
    class_class_curie: ClassVar[str] = "as:OrderedCollection"
    class_name: ClassVar[str] = "OrderedCollection"
    class_model_uri: ClassVar[URIRef] = APODS.OrderedCollection


# Enumerations
class AccessNeed(EnumDefinitionImpl):
    """
    Solid Application Interoperability Access Needs that are custom to ActivityPods.
    """
    ReadInbox = PermissibleValue(
        text="ReadInbox",
        description="Permission to read and watch the user's inbox.",
        meaning=APODS["ReadInbox"])
    ReadOutbox = PermissibleValue(
        text="ReadOutbox",
        description="Permission to read and watch the user's outbox",
        meaning=APODS["ReadOutbox"])
    PostOutbox = PermissibleValue(
        text="PostOutbox",
        description="Permission to post to the outbox as the user",
        meaning=APODS["PostOutbox"])
    CreateWacGroup = PermissibleValue(
        text="CreateWacGroup",
        description="Permission to new create Web Access Control (WAC) groups.",
        meaning=APODS["CreateWacGroup"])
    CreateCollection = PermissibleValue(
        text="CreateCollection",
        description="Permission to create new ActivityStreams collections.",
        meaning=APODS["CreateCollection"])
    QuerySparqlEndpoint = PermissibleValue(
        text="QuerySparqlEndpoint",
        description="Permission to query the Pod's SPARQL endpoint (with WAC permissions applied).",
        meaning=APODS["QuerySparqlEndpoint"])
    UpdateWebId = PermissibleValue(
        text="UpdateWebId",
        description="""Permission to modify the user's WebID resource. Caution; Only highly trusted apps should be allowed to modify the WebId.""",
        meaning=APODS["UpdateWebId"])

    _defn = EnumDefinition(
        name="AccessNeed",
        description="Solid Application Interoperability Access Needs that are custom to ActivityPods.",
    )

class SortOrder(EnumDefinitionImpl):

    AscOrder = PermissibleValue(
        text="AscOrder",
        meaning=APODS["AscOrder"])
    DescOrder = PermissibleValue(
        text="DescOrder",
        meaning=APODS["DescOrder"])

    _defn = EnumDefinition(
        name="SortOrder",
    )

class EventStatus(EnumDefinitionImpl):

    Open = PermissibleValue(
        text="Open",
        meaning=APODS["Open"])
    Coming = PermissibleValue(
        text="Coming",
        meaning=APODS["Coming"])
    Closed = PermissibleValue(
        text="Closed",
        meaning=APODS["Closed"])
    Finished = PermissibleValue(
        text="Finished",
        meaning=APODS["Finished"])

    _defn = EnumDefinition(
        name="EventStatus",
    )

# Slots
class slots:
    pass

slots.sortField = Slot(uri=APODS.sortField, name="sortField", curie=APODS.curie('sortField'),
                   model_uri=APODS.sortField, domain=None, range=Optional[str])

slots.sortOrder = Slot(uri=APODS.sortOrder, name="sortOrder", curie=APODS.curie('sortOrder'),
                   model_uri=APODS.sortOrder, domain=None, range=Optional[Union[str, "SortOrder"]])

slots.dereferenceItems = Slot(uri=APODS.dereferenceItems, name="dereferenceItems", curie=APODS.curie('dereferenceItems'),
                   model_uri=APODS.dereferenceItems, domain=None, range=Optional[Union[bool, Bool]])

slots.capabilities = Slot(uri=APODS.capabilities, name="capabilities", curie=APODS.curie('capabilities'),
                   model_uri=APODS.capabilities, domain=None, range=Optional[Union[str, URI]])

slots.area = Slot(uri=APODS.area, name="area", curie=APODS.curie('area'),
                   model_uri=APODS.area, domain=None, range=Optional[str])

slots.locales = Slot(uri=APODS.locales, name="locales", curie=APODS.curie('locales'),
                   model_uri=APODS.locales, domain=None, range=Optional[Union[str, List[str]]])

slots.baseUrl = Slot(uri=APODS.baseUrl, name="baseUrl", curie=APODS.curie('baseUrl'),
                   model_uri=APODS.baseUrl, domain=None, range=URIRef)

slots.providedBy = Slot(uri=APODS.providedBy, name="providedBy", curie=APODS.curie('providedBy'),
                   model_uri=APODS.providedBy, domain=None, range=Optional[str])

slots.contactRequests = Slot(uri=APODS.contactRequests, name="contactRequests", curie=APODS.curie('contactRequests'),
                   model_uri=APODS.contactRequests, domain=None, range=Optional[Union[str, URI]])

slots.ignoredContacts = Slot(uri=APODS.ignoredContacts, name="ignoredContacts", curie=APODS.curie('ignoredContacts'),
                   model_uri=APODS.ignoredContacts, domain=None, range=Optional[Union[str, URI]])

slots.rejectedContacts = Slot(uri=APODS.rejectedContacts, name="rejectedContacts", curie=APODS.curie('rejectedContacts'),
                   model_uri=APODS.rejectedContacts, domain=None, range=Optional[Union[str, URI]])

slots.contacts = Slot(uri=APODS.contacts, name="contacts", curie=APODS.curie('contacts'),
                   model_uri=APODS.contacts, domain=None, range=Optional[Union[str, URI]])

slots.defaultApp = Slot(uri=APODS.defaultApp, name="defaultApp", curie=APODS.curie('defaultApp'),
                   model_uri=APODS.defaultApp, domain=None, range=Optional[Union[str, URI]])

slots.icon = Slot(uri=APODS.icon, name="icon", curie=APODS.curie('icon'),
                   model_uri=APODS.icon, domain=None, range=Optional[Union[str, URI]])

slots.openEndpoint = Slot(uri=APODS.openEndpoint, name="openEndpoint", curie=APODS.curie('openEndpoint'),
                   model_uri=APODS.openEndpoint, domain=None, range=Optional[Union[str, URI]])

slots.availableApps = Slot(uri=APODS.availableApps, name="availableApps", curie=APODS.curie('availableApps'),
                   model_uri=APODS.availableApps, domain=None, range=Optional[Union[Union[str, URI], List[Union[str, URI]]]])

slots.labelPredicate = Slot(uri=APODS.labelPredicate, name="labelPredicate", curie=APODS.curie('labelPredicate'),
                   model_uri=APODS.labelPredicate, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.describedClass = Slot(uri=APODS.describedClass, name="describedClass", curie=APODS.curie('describedClass'),
                   model_uri=APODS.describedClass, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.describedBy = Slot(uri=APODS.describedBy, name="describedBy", curie=APODS.curie('describedBy'),
                   model_uri=APODS.describedBy, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.attendees = Slot(uri=APODS.attendees, name="attendees", curie=APODS.curie('attendees'),
                   model_uri=APODS.attendees, domain=None, range=Optional[Union[Union[str, URI], List[Union[str, URI]]]])

slots.maxAttendees = Slot(uri=APODS.maxAttendees, name="maxAttendees", curie=APODS.curie('maxAttendees'),
                   model_uri=APODS.maxAttendees, domain=None, range=Optional[int])

slots.closingTime = Slot(uri=APODS.closingTime, name="closingTime", curie=APODS.curie('closingTime'),
                   model_uri=APODS.closingTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.announcers = Slot(uri=APODS.announcers, name="announcers", curie=APODS.curie('announcers'),
                   model_uri=APODS.announcers, domain=None, range=Optional[Union[Union[str, URI], List[Union[str, URI]]]])

slots.announces = Slot(uri=APODS.announces, name="announces", curie=APODS.curie('announces'),
                   model_uri=APODS.announces, domain=None, range=Optional[Union[Union[str, URI], List[Union[str, URI]]]])

slots.hasFormat = Slot(uri=APODS.hasFormat, name="hasFormat", curie=APODS.curie('hasFormat'),
                   model_uri=APODS.hasFormat, domain=None, range=Optional[Union[dict, EventFormat]])

slots.hasStatus = Slot(uri=APODS.hasStatus, name="hasStatus", curie=APODS.curie('hasStatus'),
                   model_uri=APODS.hasStatus, domain=None, range=Optional[Union[str, "EventStatus"]])

slots.hasSpecialRights = Slot(uri=APODS.hasSpecialRights, name="hasSpecialRights", curie=APODS.curie('hasSpecialRights'),
                   model_uri=APODS.hasSpecialRights, domain=None, range=Optional[Union[Union[str, URI], List[Union[str, URI]]]])

slots.hasClassDescription = Slot(uri=APODS.hasClassDescription, name="hasClassDescription", curie=APODS.curie('hasClassDescription'),
                   model_uri=APODS.hasClassDescription, domain=None, range=Optional[str])

slots.registeredClass = Slot(uri=APODS.registeredClass, name="registeredClass", curie=APODS.curie('registeredClass'),
                   model_uri=APODS.registeredClass, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.registeredContainer = Slot(uri=APODS.registeredContainer, name="registeredContainer", curie=APODS.curie('registeredContainer'),
                   model_uri=APODS.registeredContainer, domain=None, range=Optional[Union[str, URI]])

slots.acceptedAccessNeeds = Slot(uri=APODS.acceptedAccessNeeds, name="acceptedAccessNeeds", curie=APODS.curie('acceptedAccessNeeds'),
                   model_uri=APODS.acceptedAccessNeeds, domain=None, range=Optional[Union[Union[str, "AccessNeed"], List[Union[str, "AccessNeed"]]]])

slots.acceptedSpecialRights = Slot(uri=APODS.acceptedSpecialRights, name="acceptedSpecialRights", curie=APODS.curie('acceptedSpecialRights'),
                   model_uri=APODS.acceptedSpecialRights, domain=None, range=Optional[Union[Union[str, "AccessNeed"], List[Union[str, "AccessNeed"]]]])

slots.preferredForTypes = Slot(uri=APODS.preferredForTypes, name="preferredForTypes", curie=APODS.curie('preferredForTypes'),
                   model_uri=APODS.preferredForTypes, domain=None, range=Optional[str])

slots.application = Slot(uri=APODS.application, name="application", curie=APODS.curie('application'),
                   model_uri=APODS.application, domain=None, range=Optional[str])

slots.preferredForClass = Slot(uri=APODS.preferredForClass, name="preferredForClass", curie=APODS.curie('preferredForClass'),
                   model_uri=APODS.preferredForClass, domain=None, range=Optional[str])

slots.prefLabel = Slot(uri=SKOS.prefLabel, name="prefLabel", curie=SKOS.curie('prefLabel'),
                   model_uri=APODS.prefLabel, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.label = Slot(uri=RDFS.label, name="label", curie=RDFS.curie('label'),
                   model_uri=APODS.label, domain=None, range=Optional[Union[str, URIorCURIE]])