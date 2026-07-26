# Selenium Basics

This folder contains the Cognizant Selenium Basics hands-on exercises and related documentation.

## Contents

- HandsOn1
  - QA Concepts, Functional Testing & Defect Lifecycle (`qa_concepts.md`)

More hands-on exercises (HandsOn2, HandsOn3, etc.) will be added in this folder.

If the Submit button ID changes from "submit" to "btn-submit", a non-POM framework requires updating every test that uses that locator.

With Page Object Model, the locator is updated only once in the page class. All tests continue to work without modification.

This improves maintainability, reduces duplication, and makes the automation framework easier to scale.