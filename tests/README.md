# Project Companion Test Suite

## Purpose

The purpose of this directory is to ensure that Project Companion
continues to behave as designed, even as it evolves.

Tests are not only for finding bugs.

They also protect the identity of the companion.

---

## Directory Structure

tests/

├── conversation/
Conversation flow and dialogue logic.

├── core/
IdentityKernel and fundamental behavior.

├── llm/
Language model abstraction and providers.

├── memory/
Memory storage and retrieval.

├── integration/
End-to-end interaction tests.

---

## Testing Philosophy

Every important behavior should eventually have a test.

Tests should describe expected behavior,
not implementation details.

A passing test means:

"The companion still behaves as intended."

---

## Future

As Project Companion grows,
this directory will expand together with it.

Testing is considered part of the design,
not an afterthought.