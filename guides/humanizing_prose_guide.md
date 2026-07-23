# De-AI-ifying Your Prose: A Practical Guide

Two different problems get lumped together as "avoiding AI detectors." Worth separating:

1. **Detector-evasion** (trying to fool a classifier) — unreliable, an arms race, and not
   what you actually need if the ideas, structure, and argument are genuinely yours (they
   are — the rubric above is about *your* thesis's argument, not generated content).
2. **Removing AI-sounding prose habits** — a real, learnable skill. LLM output has
   identifiable tics regardless of whether a detector catches them, and a human examiner
   *will* notice them. This is the one worth solving properly, because fixing it also just
   makes the writing better.

Everything below targets #2. If any passage started as AI-drafted text, the goal is to
rewrite it in your own sentence rhythm — not disguise it, replace it.

---

## 1. The Tells (in order of how often they show up in academic drafts)

| Tell | Example | Why it reads as AI |
|---|---|---|
| **Triadic lists** | "faster, cheaper, and more reliable" / "structural, semantic, and computational" | LLMs default to rule-of-three even when two items or four items fit the actual content better. Vary: sometimes one item, sometimes five, sometimes a list that trails into a subordinate clause instead of closing cleanly |
| **Hedge-then-assert rhythm** | "While X is true, it is also important to note that Y" | This exact scaffolding repeated across paragraphs is a fingerprint. Real academic hedging is uneven — sometimes you just assert, sometimes you spend a whole paragraph qualifying one claim |
| **Symmetrical "on one hand / on the other"** | Overly balanced comparisons where both sides get equal sentence length | Real arguments are lopsided. If GCR's weakness matters more than DoG's, give it more space and don't pretend it's a fair fight |
| **Stock transition words** | Furthermore, Moreover, Additionally, In addition, It is worth noting, Notably | Fine in small doses, deadly in bulk. Human academic writers often just start the next sentence with the claim — no connective tissue needed if the logic is already clear from content |
| **Empty intensifiers / vague abstraction nouns** | "This plays a crucial role in..." / "This underscores the importance of..." / "This highlights..." | These say nothing specific. Replace with the actual mechanism: not "this underscores the importance of semantic filtering" but "this is why paths scoring below τ get dropped before the trie is built" |
| **Uniform paragraph shape** | Every paragraph: topic sentence → 3 supporting sentences → wrap-up sentence | Real writing has paragraphs that are two sentences and paragraphs that run to a page, depending on how much the point needs |
| **Over-precise hedged claims** | "This suggests a potential correlation that may warrant further investigation" | Say what you actually think: "This probably explains the drop" or "I can't tell from this data whether X or Y is the cause" |
| **Summary sentences that restate instead of advance** | Ending a paragraph by rephrasing its first sentence | If the last sentence doesn't add new information or point forward, cut it |
| **Em-dash overuse for dramatic pause** | "The result was surprising — and troubling" | One or two per chapter reads fine. One per paragraph reads like a tic |
| **Latinate throat-clearing** | "It is important to note that," "It should be noted that," "One can observe that" | Delete the whole clause. Just say the thing |
| **Perfectly balanced sentence pairs** | "Not only does X increase, but Y also decreases" repeated as a pattern | Break the pattern rhythm deliberately — short sentence, then a long one with a subordinate clause, then a fragment if it earns its place |

---

## 2. Field-Specific Versions of These Tells (from your actual draft)

Watch for these exact patterns, since they show up a lot in ML/systems writing
specifically:

- **"This is not surprising, since..."** — used reflexively to explain away any result.
  Only use it when you can actually cite the specific mechanism; otherwise the result
  probably *should* surprise you, or you haven't looked hard enough.
- **"X achieves Y while maintaining Z"** — a very common LLM-generated results-sentence
  template ("DCA-Trie reduces path count while maintaining structural faithfulness").
  Vary the syntax: sometimes lead with the tradeoff, sometimes just report the number
  and let the tradeoff surface in the next sentence.
- **Every method described with identical structural template** ("Method X does A. It
  achieves B. However, it has limitation C.") across ten related-work paragraphs in a
  row. Real lit reviews vary paragraph structure by what's actually interesting about
  each paper — sometimes you lead with the limitation, sometimes with a number, sometimes
  with a quote from their own framing.
- **Section-closing "this motivates the next section" sentences on every single
  subsection** — fine once per chapter, exhausting every 400 words.

---

## 3. Concrete Fixes

1. **Read it aloud.** AI cadence is smoothest at the sentence-to-sentence level but flat
   across paragraphs. Your ear catches monotony faster than your eye does.
2. **Vary sentence length on purpose.** Take any paragraph and count words per sentence.
   If they're all within ~5 words of each other, break the pattern — one short sentence,
   one long one with a subordinate clause.
3. **Cut the last sentence of every paragraph and see if you miss it.** Often you don't —
   that sentence was doing "closure," a very AI habit, not adding content.
4. **Replace vague nouns with the specific mechanism.** Search your draft for "importance,"
   "significance," "aspect," "factor," "element" — these are almost always standing in for
   something you could just say directly.
5. **Let some claims stand unhedged.** Not everything needs "may," "potentially," "could
   suggest." If FNR is high and that explains the Hits@1 drop, say "this explains the drop,"
   not "this may partially account for the observed decrease."
6. **Write your own topic sentences first, in your own words, before expanding.** If you
   draft with AI assistance, use it for expansion/structure/citation-checking, then rewrite
   the connective and evaluative sentences (the ones that say what something *means*)
   entirely yourself — those are exactly the sentences examiners scrutinize hardest and
   exactly where AI phrasing is most detectable, because they're generic by construction.
7. **Keep your own inconsistencies.** You don't always call it "the constraint oracle" —
   sometimes you'll call it "the trie," sometimes "the filter," sometimes "the oracle
   layer." Real writers vary terminology slightly across a 90-page document even when
   being careful. Total uniformity of terminology across every chapter is itself a
   slight tell.

---

## 4. What Not to Bother With

- Don't hunt for a "detector-proof" thesaurus swap-out — replacing words with
  synonyms to dodge a classifier degrades the writing and doesn't reliably work anyway;
  detectors look at structure and predictability, not vocabulary alone.
- Don't add random typos or broken grammar to seem human — examiners notice that
  immediately and it reads as sloppy, not authentic.
- Don't over-correct into artificial casualness (contractions, slang) in a formal
  dissertation register — that's a different failure mode, and UMaT's examiners will
  flag register problems just as fast as AI-flatness.

The reliable fix isn't tricking a tool — it's making sure every evaluative sentence
(the ones claiming something *means* something, not just reporting a number) was actually
composed by you, in your own rhythm, thinking about your specific data. That's also,
not coincidentally, the exact same standard the McEnerney rubric already demands.
