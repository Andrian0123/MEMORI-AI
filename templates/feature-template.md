#date: 2026-06-23
#time: 21:03 UTC
<!-- @see templates/adr-template.md -->
---
title: Feature Template
type: feature
status: draft
priority: medium
date: <% tp.date.now("YYYY-MM-DD") %>
tags: [feature]
context: "Feature specification"
decision: ""
outcome: ""
---

# <% tp.file.title %>

## Description
<% tp.file.cursor() %>

## User Story
As a **<role>**, I want **<action>**, so that **<benefit>**

## Acceptance Criteria
- [ ] 

## Technical Details
### API
```http
GET /api/v1/...
```

### Data Model
```kotlin
data class ...
```

## Related
- [[00-INDEX]]
- [[01-ARCHITECTURE]]