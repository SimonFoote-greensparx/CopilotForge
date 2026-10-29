# Using CopilotForge with Microsoft Copilot Cowork

Copilot Cowork supports the open Agent Skills format that every CopilotForge skill is written in. You can add whole
departments as plugins, add a single skill, set custom instructions, and build a tailored transformation pack whose
documents land in your own OneDrive. Cowork changes regularly; if a menu has moved, follow Microsoft's current guidance
(source record `ms-copilot-cowork-customise`).

## Before you start

- You need Copilot Cowork in your tenant, and your organisation must allow you to upload your own plugins and skills.
  If **Upload plugin** is missing, ask your Microsoft 365 administrator.
- Skills run as instructions to the AI. Read what you upload; every skill here is plain text.
- Every skill is currently `status: draft` (walking skeleton). Treat the advice as a practitioner's first draft.

## Add departments as plugins

1. Choose the departments you need (table below).
2. Download `cowork/plugins/copilotforge-<department>.zip` from the repository.
3. In Copilot Cowork select **Customize** > **Plugins** > **Upload plugin** and choose the archive.
4. Share it with **Only you** to try it, or with specific colleagues.
5. Start a new conversation.

| If you want to... | Upload |
|---|---|
| Design your whole Microsoft AI programme | `copilotforge-organisation-tailoring`, `copilotforge-ai-strategy`, `copilotforge-copilot-adoption`, `copilotforge-champions`, `copilotforge-ai-centre-of-excellence`, `copilotforge-opportunity-management`, `copilotforge-m365-agents`, `copilotforge-security-privacy` |
| Fix inconsistent Copilot use | `copilotforge-copilot-adoption`, `copilotforge-champions` |
| Set up an AI Centre of Excellence | `copilotforge-ai-centre-of-excellence`, `copilotforge-opportunity-management`, `copilotforge-security-privacy` |
| Bring departmental agents under control | `copilotforge-m365-agents`, `copilotforge-opportunity-management`, `copilotforge-security-privacy` |

Install only what you need: Cowork reads every installed skill's description when choosing one, so a focused set gives
sharper results. Plugin names start with `copilotforge-`, so they sit alongside other skill libraries without clashing.

## Build a tailored transformation pack

1. Upload the plugins for designing a whole programme (first row above).
2. Create an organisation profile: start from a fictional sample in `profiles/samples/`, or let the
   `ai-profile-intake` skill interview you. Use roles and aliases, not names.
3. Keep the profile in your own OneDrive. Never in a shared or public location.
4. In a new conversation, attach the profile and ask: "Design our Microsoft AI programme from this profile."
5. Confirm the recommended edition, archetype and ownership map before the pack is written.
6. When the profile changes, ask for a refresh; the refresh explains what changed rather than silently replacing your edits.

## Suggested custom instructions

Copy [`cowork/custom-instructions.md`](../cowork/custom-instructions.md) into **Customize** > **Preferences**.
