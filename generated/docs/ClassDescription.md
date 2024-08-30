
# Class: ClassDescription

Description of an RDFS class used in Type Registration

URI: [apods:ClassDescription](https://activitypods.org/ns/core#ClassDescription)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ClassDescription&#124;icon:uri%20%3F;openEndpoint:uri%20%3F;labelPredicate:uriorcurie%20%3F;describedClass:uriorcurie%20%3F;describedBy:uriorcurie%20%3F;prefLabel:uriorcurie%20%3F])](https://yuml.me/diagram/nofunky;dir:TB/class/[ClassDescription&#124;icon:uri%20%3F;openEndpoint:uri%20%3F;labelPredicate:uriorcurie%20%3F;describedClass:uriorcurie%20%3F;describedBy:uriorcurie%20%3F;prefLabel:uriorcurie%20%3F])

## Attributes


### Own

 * [icon](icon.md)  <sub>0..1</sub>
     * Description: The icon to show for a resource's class.
     * Range: [Uri](types/Uri.md)
 * [openEndpoint](openEndpoint.md)  <sub>0..1</sub>
     * Range: [Uri](types/Uri.md)
 * [labelPredicate](labelPredicate.md)  <sub>0..1</sub>
     * Description: The predicate used as a human-readable label for resources of a given class
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [describedClass](describedClass.md)  <sub>0..1</sub>
     * Description: The class described by a ClassDescription
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [describedBy](describedBy.md)  <sub>0..1</sub>
     * Description: The app registering a given ClassDescription.
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [prefLabel](prefLabel.md)  <sub>0..1</sub>
     * Range: [Uriorcurie](types/Uriorcurie.md)
