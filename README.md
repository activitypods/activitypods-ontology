# Activitypods Ontology

[LinkML](https://linkml.io/) ontology for ActivityPods.

## Repository Structure

- [generated/](generated/) - Generated schema files, e.g. in owl, json-schema, or shacl (do not edit these)
- [src/](src/) - source files (edit these)
  - [linkml_activitypods/activitypods-ontology.yaml](src/linkml_activitypods/activitypods-ontology.yaml) - The schema definition file

## Developer Documentation

Use the `make` command to generate project artifacts:

- `make gen-project`: Generate the schema files.

## Notes

This repository is work in progress. In the future, it is intended to be used for general definitions that help to improve typing RDF data used in ActivityPods.
