# ci-artifact-hashing

Reproducible SHA-256 digests for CI artifacts (scan outputs, reports) so an original can be
compared byte-for-byte against a retained copy later.

    python digest.py artifacts/ > digests.txt

Maintainer: Daniel Kessler (clearaudit)
