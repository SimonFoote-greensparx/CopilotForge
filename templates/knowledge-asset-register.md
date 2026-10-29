# Knowledge asset register

Template id: `knowledge-asset-register`
Responsible skill: `knowledge-management:knowledge-inventory`

Use this register to record the organisation's knowledge sources: where each one lives, who owns it, who should see it,
what condition it is in and which Copilot scenarios or agents depend on it. Other knowledge skills update it, notably
`knowledge-management:knowledge-classification`, `knowledge-management:knowledge-review-cycles` and
`knowledge-management:knowledge-grounding-standards`. Every fact the organisation must supply is marked
`[To confirm: ...]`; replace the marker when the fact is confirmed and never fill it with a guess. Example rows are
fictional and are there to be replaced or deleted.

## 1. Register details

| Field | Value |
|---|---|
| Scope (domains, business units) | [To confirm: scope] |
| Register owner (role) | [To confirm: usually the Knowledge Manager] |
| Unit of inventory | [To confirm: library, site or curated collection, and why] |
| Where the register is held | [To confirm: for example a SharePoint list] |
| Who may edit entries | [To confirm: content owners for their own rows, knowledge team for all] |
| Overdue entry chase routine | [To confirm: frequency and role] |
| Last full verification sample | [To confirm: date and result] |

## 2. Field definitions

| Field | Definition | Mandatory |
|---|---|---|
| ID | Unique reference, never reused | Yes |
| Name | The name people use for the source | Yes |
| Location | Site, library, page set, connector or system | Yes |
| Source type | Library, page set, curated collection, connector content, public website, uploaded files | Yes |
| Domain | The knowledge domain the source belongs to | Yes |
| Domain owner (role) | Accountable for what the organisation treats as true in the domain | Yes |
| Content owner (role) and acceptance | Accountable for accuracy, currency and audience; record whether the role has been accepted | Yes |
| Deputy (role) | Covers absence and succession | Yes for AI-dependent sources |
| Administrative owner (role) | Controls platform permissions and configuration; not accountable for accuracy | Yes |
| Intended audience | Who should be able to see the content, in plain words | Yes |
| Actual access | Who can open it today, from administrative data | Yes |
| Sensitivity | Value from the organisation's classification scheme | Yes |
| Knowledge status | Authoritative, reference, working or archive | Yes |
| Condition rating | 1 to 4 on the readiness dimensions, with date | Yes |
| Quality rating | Good, fair or poor, with date of last check | Where checked |
| Last review / next review | Dates from the review cycle | Yes |
| Review triggers | Events that force an early review | Where set |
| Grounding designation | Approved to tier N, with expiry, or not approved | Where designated |
| Dependent AI uses | Agents, Copilot scenarios and curated collections that rely on the source | Yes |
| Findings and referrals | Open findings and where they were routed | Where any |

## 3. Register

| ID | Name | Location | Type | Domain | Content owner (accepted?) | Intended audience | Actual access | Sensitivity | Status | Condition | Next review | Designation | Dependent AI uses |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| KA-001 (fictional example) | HR policies | HR site, Policies library | Library | HR policy | Head of reward (accepted) | All staff | All staff | Internal | Authoritative | 3 | [To confirm: date] | Approved to tier 2, expires with review | Absence policy agent; Copilot HR scenarios |
| KA-002 (fictional example) | HR shared drafts | HR site, Shared folder | Library | HR policy | [To confirm: owner] (not accepted) | HR team | All staff | Confidential | Working | 1 | [To confirm: date] | Not approved | None; access mismatch referred |
| [To confirm: ID] | [To confirm: name] | [To confirm: location] | [To confirm: type] | [To confirm: domain] | [To confirm: role and acceptance] | [To confirm: audience] | [To confirm: actual access] | [To confirm: sensitivity] | [To confirm: status] | [To confirm: 1-4] | [To confirm: date] | [To confirm: designation] | [To confirm: dependent uses] |

## 4. Blind spots

Locations deliberately not registered, and why.

| Location or type | Reason not registered | Risk noted |
|---|---|---|
| Personal drives and chats | Not knowledge sources; recorded as a blind spot | [To confirm: risk] |
| [To confirm: location] | [To confirm: reason] | [To confirm: risk] |

## 5. Open findings

| Ref | Source ID | Finding (missing owner, access mismatch, competing version, other) | Routed to | Owner (role) | Due |
|---|---|---|---|---|---|
| F1 | [To confirm: ID] | [To confirm: finding] | [To confirm: skill or team] | [To confirm: role] | [To confirm: date] |

## 6. Change log

| Date | Change | By (role) |
|---|---|---|
| [To confirm: date] | [To confirm: change] | [To confirm: role] |

> Credit: Template from CopilotForge by Simon Foote (https://github.com/SimonFoote-greensparx/CopilotForge), licensed under CC BY 4.0. Keep this credit when you share or adapt the template; in your own completed document you may keep it as a footer or remove it.
