
# Class: PodProvider

General information about a pod provider

URI: [apods:PodProvider](https://activitypods.org/ns/core#PodProvider)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[PodProvider&#124;area:string%20%3F;locales:string%20*;baseUrl:uri;providedBy:string%20%3F])](https://yuml.me/diagram/nofunky;dir:TB/class/[PodProvider&#124;area:string%20%3F;locales:string%20*;baseUrl:uri;providedBy:string%20%3F])

## Attributes


### Own

 * [area](area.md)  <sub>0..1</sub>
     * Description: A human-readable location string of a Pod Provider.
     * Range: [String](types/String.md)
 * [locales](locales.md)  <sub>0..\*</sub>
     * Description: A set of supported locale language tags of a Pod Provider.
     * Range: [String](types/String.md)
 * [baseUrl](baseUrl.md)  <sub>1..1</sub>
     * Description: The base URL of a Pod Provider.
     * Range: [Uri](types/Uri.md)
 * [providedBy](providedBy.md)  <sub>0..1</sub>
     * Description: The instance name of the Pod Provider
     * Range: [String](types/String.md)
