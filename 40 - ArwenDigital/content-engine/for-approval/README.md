---
tags: [content-engine, approval-queue]
status: active
---

# For Approval

This folder should contain only content Arnold still needs to approve.

- Blog drafts waiting for Arnold: save here.
- Social packs waiting for Arnold: save here.
- If there is nothing to approve, this folder should be empty except this README.

After Arnold says `approved blog`, move the approved blog file to `../blog-approved/`.
After Arnold says `approved social`, move the approved social pack to `../approved-social/`.

Cron jobs should publish/schedule only from the approved folders, never directly from `for-approval`.
