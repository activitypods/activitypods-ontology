
# activitypods-ontology


**metamodel version:** 1.7.0

**version:** None


LinkML ontology for ActivityPods


### Classes

 * [Activity](Activity.md)
     * [Install](Install.md) - Activity to Install an app using Solid Application Interoperability
     * [Notification](Notification.md) - A notification activity from an app to notify the user.
 * [ClassDescription](ClassDescription.md) - Description of an RDFS class used in Type Registration
 * [Collection](Collection.md)
 * [EventFormat](EventFormat.md)
 * [OrderedCollection](OrderedCollection.md)
 * [PodProvider](PodProvider.md) - General information about a pod provider

### Mixins


### Slots

 * [acceptedAccessNeeds](acceptedAccessNeeds.md) - The access needs accepted in an app registration.
 * [acceptedSpecialRights](acceptedSpecialRights.md) - The special access needs accepted in an app registration.
 * [announcers](announcers.md) - The set of actors authorized to announce an activity
 * [announces](announces.md) - The set of actors authorized to view an activity
 * [application](application.md)
 * [area](area.md) - A human-readable location string of a Pod Provider.
 * [attendees](attendees.md) - The set of a attendees of an event
 * [availableApps](availableApps.md) - The available apps that are capable of handling a given class
 * [baseUrl](baseUrl.md) - The base URL of a Pod Provider.
 * [capabilities](capabilities.md) - URI to an actor's container of capabilities. This should be referenced from an actor's WebID.
 * [closingTime](closingTime.md) - The datetime at which no new attendees can join an activity
 * [contactRequests](contactRequests.md) - Collection of contact requests to an ActivityPub actor
 * [contacts](contacts.md) - Collection of contacts of an ActivityPub actor
 * [defaultApp](defaultApp.md) - The default app to open a resource of a given RDFS class with.
 * [dereferenceItems](dereferenceItems.md)
 * [describedBy](describedBy.md) - The app registering a given ClassDescription.
 * [describedClass](describedClass.md) - The class described by a ClassDescription
 * [hasClassDescription](hasClassDescription.md)
 * [hasFormat](hasFormat.md) - The EventFormat type of an event (e.g. a movie night).
 * [hasSpecialRights](hasSpecialRights.md)
 * [hasStatus](hasStatus.md) - The lifecycle status of the event (e.g. open or finished).
 * [icon](icon.md) - The icon to show for a resource's class.
 * [ignoredContacts](ignoredContacts.md) - Collection of contacts ignored by an ActivityPub actor
 * [label](label.md)
 * [labelPredicate](labelPredicate.md) - The predicate used as a human-readable label for resources of a given class
 * [locales](locales.md) - A set of supported locale language tags of a Pod Provider.
 * [maxAttendees](maxAttendees.md) - The maximum number of actors that are allowed to participate in an event.
 * [openEndpoint](openEndpoint.md)
 * [prefLabel](prefLabel.md)
 * [preferredForClass](preferredForClass.md)
 * [preferredForTypes](preferredForTypes.md)
 * [providedBy](providedBy.md) - The instance name of the Pod Provider
 * [registeredClass](registeredClass.md) - Class registered by an app to whose resources it has certain access rights.
 * [registeredContainer](registeredContainer.md) - The container that contains a registered type's resources from a type registration.
 * [rejectedContacts](rejectedContacts.md) - Collection of contact requests rejected by an ActivityPub actor
 * [sortField](sortField.md) - The RDF property to order the collection by
 * [sortOrder](sortOrder.md) - The sort order of a collection

### Enums

 * [AccessNeed](AccessNeed.md) - Solid Application Interoperability Access Needs that are custom to ActivityPods.
 * [EventStatus](EventStatus.md)
 * [SortOrder](SortOrder.md)

### Subsets


### Types


#### Built in

 * **Bool**
 * **Curie**
 * **Decimal**
 * **ElementIdentifier**
 * **NCName**
 * **NodeIdentifier**
 * **URI**
 * **URIorCURIE**
 * **XSDDate**
 * **XSDDateTime**
 * **XSDTime**
 * **float**
 * **int**
 * **str**

#### Defined

 * [Boolean](types/Boolean.md)  (**Bool**)  - A binary (true or false) value
 * [Curie](types/Curie.md)  (**Curie**)  - a compact URI
 * [Date](types/Date.md)  (**XSDDate**)  - a date (year, month and day) in an idealized calendar
 * [DateOrDatetime](types/DateOrDatetime.md)  (**str**)  - Either a date or a datetime
 * [Datetime](types/Datetime.md)  (**XSDDateTime**)  - The combination of a date and time
 * [Decimal](types/Decimal.md)  (**Decimal**)  - A real number with arbitrary precision that conforms to the xsd:decimal specification
 * [Double](types/Double.md)  (**float**)  - A real number that conforms to the xsd:double specification
 * [Float](types/Float.md)  (**float**)  - A real number that conforms to the xsd:float specification
 * [Integer](types/Integer.md)  (**int**)  - An integer
 * [Jsonpath](types/Jsonpath.md)  (**str**)  - A string encoding a JSON Path. The value of the string MUST conform to JSON Point syntax and SHOULD dereference to zero or more valid objects within the current instance document when encoded in tree form.
 * [Jsonpointer](types/Jsonpointer.md)  (**str**)  - A string encoding a JSON Pointer. The value of the string MUST conform to JSON Point syntax and SHOULD dereference to a valid object within the current instance document when encoded in tree form.
 * [Ncname](types/Ncname.md)  (**NCName**)  - Prefix part of CURIE
 * [Nodeidentifier](types/Nodeidentifier.md)  (**NodeIdentifier**)  - A URI, CURIE or BNODE that represents a node in a model.
 * [Objectidentifier](types/Objectidentifier.md)  (**ElementIdentifier**)  - A URI or CURIE that represents an object in the model.
 * [Sparqlpath](types/Sparqlpath.md)  (**str**)  - A string encoding a SPARQL Property Path. The value of the string MUST conform to SPARQL syntax and SHOULD dereference to zero or more valid objects within the current instance document when encoded as RDF.
 * [String](types/String.md)  (**str**)  - A character string
 * [Time](types/Time.md)  (**XSDTime**)  - A time object represents a (local) time of day, independent of any particular day
 * [Uri](types/Uri.md)  (**URI**)  - a complete URI
 * [Uriorcurie](types/Uriorcurie.md)  (**URIorCURIE**)  - a URI or a CURIE
