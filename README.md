# Media-Validation
THis project is to assess the validity of certain sources through using NLP to
cross-reference each of them with various sources in the industry, presenting a “validity
score” of sorts for common media outlets nationwide. For this, we plan to gather data
from a variety of sources, some of which we can label as misinformation. We will also
have an official “source of truth” which, for the sake of this algorithm, will be
government-provided information. Using this source of truth, we can then label facts and
information in other outlets to be conflicting or aligned with the source. Each conflict
will be penalized and each alignment rewarded - thus contributing to a source-specific
“truth score” as a result for each source.