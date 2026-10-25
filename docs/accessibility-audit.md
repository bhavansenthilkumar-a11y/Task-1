# Accessibility Baseline & Repository Architecture Audit

## 1. Website Details

- **Website:** National Portal of India
- **URL:** https://www.india.gov.in/
- **Audit Tool:** Google Chrome Lighthouse
- **Audit Type:** Accessibility, Performance, Best Practices and SEO

## 2. Lighthouse Scores

| Category | Score |
|---|---:|
| Performance | 49 |
| Accessibility | 89 |
| Best Practices | 88 |
| SEO | 100 |

## 3. Accessibility and Architecture Findings

### Issue 1: Incorrect ARIA List Structure

**Category:** Accessibility — ARIA

**Issue Description:**  
Lighthouse reports that some ARIA child roles are not contained by their required parent elements. The affected elements use `role="listitem"` without the required parent role `list`.

**Evidence:**  
The Lighthouse Accessibility audit identifies the following failing elements:

- `<div role="listitem" id="topBarServiceList">`
- `<ul role="listitem" id="footerCategoryList">`
- `<ul role="listitem" id="footerCategoryListSecondSection">`
- `<ul role="listitem" id="footerMyGovernmentList">`
- `<ul role="listitem" id="footerExploreBharatList">`
- `<ul role="listitem" id="footerOtherList">`
- `<ul role="listitem" id="footerOtherListSecondSection">`

**Impact:**  
Incorrect ARIA roles can make list relationships difficult for assistive technologies to interpret correctly, affecting users who rely on screen readers.

**Priority:** High

**Recommended Remediation:**  
Use semantic HTML list elements and correct ARIA roles. List items should be contained within a parent list. For example, use `<ul>` as the list container and `<li>` for individual items. Remove incorrect ARIA roles when native HTML semantics already provide the required accessibility information.

**Screenshot Evidence:**  
`docs/screenshots/individual-issues/issue-01-aria.png`

**Status:** Identified — remediation recommended.


### Issue 2: Insufficient Colour Contrast

**Category:** Accessibility — Colour Contrast

**Issue Description:**  
Lighthouse identifies low-contrast text on the National Portal of India website. Some text elements may not have sufficient contrast between the foreground text colour and the background colour, making the content difficult for users with low vision or colour-vision deficiencies to read.

**Evidence:**  
The Lighthouse Accessibility audit identifies the following failing elements:

- `CENTRAL GOVERNMENT`
- `1,097+ CENTRAL GOVERNMENT`
- `STATE GOVERNMENT`
- `12,448+ STATE GOVERNMENT`
- `IMPORTANT SERVICES`
- `33 IMPORTANT SERVICES`
- `INFORMATION CATEGORIES`
- `18 INFORMATION CATEGORIES`
- `Avail online Services & Save time`
- `Online Services` section

**Impact:**  
Insufficient colour contrast can reduce text readability, particularly for users with low vision or other visual impairments.

**Priority:** High

**Recommended Remediation:**  
Adjust the foreground text and background colours to achieve sufficient contrast. For normal text, target a contrast ratio of at least 4.5:1. For large text, target at least 3:1, in accordance with WCAG 2.2 Level AA contrast requirements. Re-test the affected elements after making changes.

**Screenshot Evidence:**  
`docs/screenshots/individual-issues/issue-02-contrast.png`

**Status:** Identified — remediation recommended.


### Issue 3: Incorrect HTML List Structure

- **Category:** Accessibility
- **Evidence:** Lighthouse reports that list items (`<li>`) are not contained within `<ul>`, `<ol>`, or `<menu>` parent elements.
- **Affected Elements:** News article links using the `newsCardList` ID.
- **Priority:** Medium
- **Recommended Fix:** Wrap list items in an appropriate `<ul>` or `<ol>` parent element, or use semantic HTML elements suitable for the content.
- **Screenshot:** `docs/screenshots/issue-03-list-structure.png`


### Issue 4: Duplicate HTML IDs

**Category:** HTML Structure / Maintainability

**Evidence:** Multiple news-card `<li>` elements use the same `id="newsCardList"` attribute.

**Impact:** HTML IDs should be unique within a document. Duplicate IDs can cause JavaScript selectors, element targeting, and accessibility relationships to behave unexpectedly.

**Priority:** Medium

**Recommended remediation:** Replace the repeated ID with a shared class if the elements represent the same type of component. Use unique IDs only when individual element identification is necessary.

**Suggested fix:**
```html
<li class="news-card">...</li>
<li class="news-card">...</li>
```

**Screenshot:** `docs/screenshots/individual-issues/issue-04-duplicate-ids.png`
o
### Issue 5: Identical Link Text with Different Destinations

- **Category:** Accessibility
- **Evidence:** Lighthouse identifies multiple links labelled “Travel & Tourism” that point to different destinations.
- **Affected Elements:**
  - `exploreCategoryCardLink` — `/category/travel-tourism`
  - `Travel & Tourism exploreBharatCardLink` — `/explore-india/travel-and-tourism`
  - `Travel & Tourism-footerCategoryListItemLink` — `/category/travel-tourism`
  - `footerExploreBharatListItemLink` — `/explore-india/travel-and-tourism`
- **Impact:** Users, especially screen-reader users navigating through links, may find it difficult to distinguish links with identical text but different destinations.
- **Priority:** Medium
- **Recommended Fix:** Make link text descriptive enough to distinguish different destinations. For example, use “Travel & Tourism Services” and “Explore Travel & Tourism in India” where those labels accurately describe the destination.
- **Screenshot:** `docs/screenshots/individual-issues/issue-05-identical-links.png`

## 4. Audit Summary

The initial Lighthouse audit recorded an accessibility score of 89, a performance score of 49, a best practices score of 88, and an SEO score of 100.

Further inspection and keyboard-only testing will be used to document five verified accessibility or architecture issues, along with evidence, remediation priorities, and recommended fixes.
