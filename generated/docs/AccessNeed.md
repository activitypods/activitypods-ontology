
# Enum: AccessNeed

Solid Application Interoperability Access Needs that are custom to ActivityPods.

URI: [apods:AccessNeed](https://activitypods.org/ns/core#AccessNeed)


## Permissible Values

| Text | Description | Meaning | Other Information |
| :--- | :---: | :---: | ---: |
| ReadInbox | Permission to read and watch the user's inbox. | apods:ReadInbox | {'title': 'Read Inbox Access Need'} |
| ReadOutbox | Permission to read and watch the user's outbox | apods:ReadOutbox | {'title': 'Read Outbox Access Need'} |
| PostOutbox | Permission to post to the outbox as the user | apods:PostOutbox | {'title': 'Post to Outbox Access Need'} |
| CreateWacGroup | Permission to new create Web Access Control (WAC) groups. | apods:CreateWacGroup | {'title': 'Create WAC Group Access Need'} |
| CreateCollection | Permission to create new ActivityStreams collections. | apods:CreateCollection | {'title': 'Create Collection Access Need'} |
| QuerySparqlEndpoint | Permission to query the Pod's SPARQL endpoint (with WAC permissions applied). | apods:QuerySparqlEndpoint | {'title': 'Query SPARQL Database Access Need'} |
| UpdateWebId | Permission to modify the user's WebID resource. Caution; Only highly trusted apps should be allowed to modify the WebId. | apods:UpdateWebId | {'title': "Modify Users's WebId Access Need"} |



## Other properties

|  |  |  |
| --- | --- | --- |
| **See also:** | | [https://docs.activitypods.org/app-framework/backend/application-registration/#special-rights](https://docs.activitypods.org/app-framework/backend/application-registration/#special-rights) |
|  | | [https://solid.github.io/data-interoperability-panel/primer/application.html](https://solid.github.io/data-interoperability-panel/primer/application.html) |