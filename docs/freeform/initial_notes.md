Chase's quick/messy prep for first meeting:
https://docs.google.com/document/d/11prgVd0fO7ExJUPIfpIdOxNnu9JivufxvUA82k1K6II/edit?usp=sharing

## GUI

- GUI similar to `synthaser` would lower the barrier for contribution
  - Used to produce standardized output (e.g. JSON)
  - Input is HMM models? Order of models/rules?
    - Snag: people would have to use models that can be distributed (e.g. PRISM HMM models are available but cannot be redistributed)
  - Could run validation of HMM/rule against an input locus/sequence


## Database format:
 
Is this one format or two (HMM's & Rules)?

- [Chase's Note]: Bacause in HMMER profile HMM files `ACC` is optional while `NAME` is required I've been hashing HMM models (just the model/emission/transition block) so I can reduce redundant models across HMM sources (e.g. model overlap between antiSMASH and PFAM). May be worth considering and is why it may be beneficial to have the info about HMMs stored separately from the rule info?
  - http://eddylab.org/software/hmmer/Userguide.pdf  p. 209

### JSON

 Note: Keys/values/etc should, at minimum, describe the functionality covered by: https://github.com/antismash/antismash/blob/master/antismash/common/hmm_rule_parser/rule_parser.py






