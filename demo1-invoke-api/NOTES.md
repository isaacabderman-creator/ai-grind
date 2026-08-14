Meeting – Q3 Product Review
Date: Thursday afternoon
Attendees: Sarah (PM), Jake (Eng Lead), Priya (Design), Tom (QA)

Started about 10 minutes late. Sarah opened by saying the search feature is running
roughly two weeks behind schedule because the ranking algorithm keeps failing QA.
Tom confirmed three test cases are still red.

Jake said the core indexing work is done and the delay is entirely on ranking.
He proposed cutting the fuzzy-match feature from v1 and shipping exact-match only
to hit the release date. Sarah agreed; fuzzy-match moves to the backlog.

Priya raised a concern: the empty-state illustration hasn't been reviewed yet.
Sarah asked Priya to share it in Slack by Friday EOD for async feedback.

Budget question came up: Jake mentioned the new search infrastructure will add
roughly $2000/month to the AWS bill. Sarah said she'd confirm with Finance
whether that fits Q3 budget before the next sprint.

Wrap-up: next sync same time next week.
