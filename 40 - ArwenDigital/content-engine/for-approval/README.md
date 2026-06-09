---
tags: [content-engine, approval-queue]
status: active
---

# For Approval

This folder should contain only content Arnold still needs to approve.

- Blog drafts waiting for Arnold: save here.
- Social packs waiting for Arnold: save here.
- If there is nothing to approve, this folder should be empty except this README.

After Arnold says `approved blog`, approve all pending blog drafts in this folder, create/update them on Bear Blog, and post/publish them with future dates assigned from the active blog schedule. Then archive/update local copies in `../blog-approved/` with Bear IDs/URLs/status.
After Arnold says `approved social`, move the approved social pack to `../approved-social/`.

Cron jobs should not publish/schedule directly from `for-approval` unless Arnold has just given an explicit approval command in the current chat.
