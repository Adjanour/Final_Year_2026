# Defense Prep — DCA-Trie Thesis

Scope note: this focuses on **DCA-Trie v1** (the validated result set: 86.4% Hits@1,
SIR 1.0→0.145, FNR<5%). v2 (dynamic expansion) is a documented negative result —
useful in Q&A if asked, not something to lead with, per the decision to avoid
scope creep before the defense.

---

## 1. Talk Track

Say these in your own words — don't read them verbatim, but the shape and the
numbers should stay fixed.

**Methodology (one breath):**
> GCR builds one static trie of every KG path before decoding starts, so the LLM
> has to use its own judgment to skip irrelevant-but-valid paths — the same
> mechanism that causes hallucination. I added TypeOracle: two symbolic gates
> (`range_gate` checks the relation's expected type, `type_gate` checks the
> terminal entity against the question's inferred answer type) that filter paths
> *before* the trie is built. No embeddings, no threshold to tune, O(1) per
> candidate triple.

**Results (one breath):**
> TypeOracle cuts the path space by 14.5% and removes 85.5% of semantically
> irrelevant paths (SIR 1.0 → 0.145) while keeping false-negative rate under 5%
> (3.3% type gate, 2.9% range gate) — so structurally it does exactly what it's
> designed to do. But Hits@1 still drops 5.2 points (91.6% → 86.4%). That drop
> is the finding, not something to apologize for.

**Evaluation (one breath):**
> I didn't stop at "it got worse." I traced it to four mechanisms — gold-path
> exclusion, beam competition changes, noise from the regex-based type
> inference, and an inherent precision/recall trade-off — so the negative
> result is explained, not just reported.

**The reframe line, if pushed on "so it's worse than baseline":**
> GCR and DoG both assume tighter structural constraints are free wins. My
> results are the first direct evidence that constraint tightness and answer
> accuracy are decoupled — that's a claim about the field's assumption, and it
> holds regardless of whether my specific gate implementation is optimal.

---

## 2. Anticipated Hard Questions

**Q: Your system performs worse than the baseline (86.4% vs 91.6%). Why is this a contribution?**
> Because no prior work (GCR, DoG) measured constraint quality independently of
> answer accuracy — they assumed the two move together. I built a metric (SIR)
> that isolates constraint quality, showed TypeOracle improves it by 85.5%, and
> showed accuracy drops anyway. That's evidence the assumption is false, which
> is more useful to the field than an unexplained accuracy bump would have
> been.

**Q: How do you know the gates are correctly implemented and not just buggy?**
> FNR is measured and decomposed per gate (3.3% type, 2.9% range) — both under
> the 5% design threshold. The gates are doing exactly what they're specified
> to do: removing paths whose type doesn't match. The accuracy drop is a
> measured side effect of correct pruning, not evidence of a bug.

**Q: Why not evaluate on the full CWQ set / larger N?**
> [Check your own methodology/limitations section for the exact N and
> variance caveat you reported, and state it plainly — this is a resource
> and time constraint of a single-semester undergrad project, already flagged
> as a recommendation for future work.] WebQSP — the primary benchmark — got
> the full 1,628-query test set; CWQ was an exploratory generalization check.

**Q: Why didn't you empirically re-run DoG for a head-to-head comparison instead of a table?**
> DoG's dynamic decoding needs its own decoding engine and infrastructure;
> reimplementing it was out of scope for a single-semester project focused on
> extending GCR directly, since GCR is the base I'm building on. The
> comparison in Chapter 4 positions DCA-Trie against both on mechanism
> (faithfulness, dynamic expansion, semantic filtering), which is the honest
> scope for this work.

**Q: DCA-Trie v2 dropped to 54% — doesn't that undermine confidence in the whole approach?**
> v1 and v2 test different hypotheses. v1 asks "does static semantic filtering
> help" — answered, with nuance. v2 asks "does *dynamic* per-hop filtering
> help," and it fails for five identified reasons (no global path context, no
> backtracking, decoding-engine mismatch, brittle entity extraction, prompt
> accumulation). That's a scoped, explained negative result, not a collapse of
> the method — v1 doesn't depend on v2 working.

**Q: Isn't "tighter constraints don't automatically help" an obvious result?**
> It contradicts an assumption stated or implied in both papers I'm extending.
> Nobody had measured it directly before because there was no metric to
> decouple constraint tightness from answer accuracy — that's what SIR is for.

**Q: What's the practical value if it doesn't improve accuracy?**
> Three things: (1) SIR itself, as a diagnostic other researchers can apply to
> their own oracles; (2) full interpretability — every exclusion has a named
> reason (range_gate/type_gate), visible in the demo, versus GCR's opaque
> full-path admission; (3) the overhead is negligible (<0.5% latency, <2MB
> memory), so it costs nothing to try even where its effect is
> context-dependent.

**Q: How generalizable is this beyond Freebase/WebQSP?**
> The gate mechanism itself is KG-agnostic — it needs a schema with relation
> ranges and entity types, which most curated KGs have. The hand-curated
> 38-relation schema is Freebase-specific and is a named limitation; the
> auto-mined schema path is what would port to a new KG.

---

## 3. Presentation (`final_project_ppt/main.tex`) — Suggestions

**Done already:**
- Fixed a typo in the title: "Graph-Constained" → "Graph-Constrained" (was on
  the title slide, the most visible line in the whole deck).

**Worth doing before the defense:**
1. **Add a backup slide right after "Demonstration"** with 2–3 screenshots of
   the actual demo app (question → gates → admitted/rejected paths → answer)
   for the "who was richard nixon married to" example (see §4 — it's your
   best story case, 24.7% of paths rejected, correct answer still found). If
   the live app breaks or there's no Wi-Fi/projector HDMI issue, you present
   from the slide instead of standing there debugging.
2. **Add a one-line "Limitations" slide** before Recommendations (currently
   limitations are only implicit inside Recommendations). Examiners read a
   dedicated limitations slide as a sign of rigor, not weakness — e.g. regex
   type inference noise, Freebase-specific hand-curated schema, CWQ sample
   size.
3. **Minor:** the "GCR vs DCA-Trie: Comparison" table lists "Hits@1" and
   "Accuracy" as two separate rows — they're the same metric here, so an
   examiner may flag it as redundant/inflating the table. Consider merging
   into one row.
4. **Minor:** in the Methodology tikz figure, the Trump edge is labeled
   `Marry_to` while the Bush/Obama edges are labeled `Spouse_of` — looks like
   a copy-paste inconsistency in an otherwise clean diagram. Harmless but easy
   to fix.

---

## 4. Running the Demo

**What it is:** `demo/app.py`, a Streamlit app. Loads pre-computed pipeline
traces for real WebQSP test questions — no GPU needed, so it's safe to run on
a laptop during the defense.

**To run it:**
```bash
cd /home/bernard/research/projects/graph-constrained-reasoning
uv run streamlit run demo/app.py
```
Opens at `http://localhost:8501`. Test this on the actual defense laptop
*before* the day — confirm `uv` and the project's `.venv`/lockfile are present
and it launches within a few seconds.

**Bug found and fixed today:** the original 10 pre-generated samples showed
**zero rejected paths on every single question** — the gate logic looked
inert. Root cause: `demo/generate_demo_data.py` called
`oracle.infer_answer_types_from_paths()` directly, which derives "answer
types" as the union of every terminal entity's type across all candidate
paths — a set that trivially contains every path's own terminal type, making
the gate vacuous. Your real experiment code (`trie_utils.py`) calls the
question-based `oracle.infer_answer_types(question)` first and only falls
back to the path-based method if that returns empty. Fixed
`generate_demo_data.py` to match, regenerated 20 samples — most now show
8–37% rejection rates, matching the real pipeline's behavior. This wasn't
committed yet; review with `git diff demo/generate_demo_data.py` and commit
when ready.

**Recommended flagship question: "who was richard nixon married to" (sample_006).**
- 2,819 candidate paths → 697 rejected (24.7%)
- Correct answer (**Pat Nixon**) is still reachable via an admitted path:
  `Richard Nixon → people.person.children → Tricia Nixon Cox → people.person.parents → Pat Nixon`
- Rejected paths are visibly nonsensical for the question: loops through
  Nixon's *quotations*, his *education record*, his *inauguration* — real KG
  paths that GCR's baseline would keep and hand to the LLM to filter itself.
- Bonus: this mirrors the spouse-relation example already on your
  Methodology slide (Bush/Obama/Trump), so the demo reads as a direct
  callback instead of a new example the audience has to re-orient around.

**Other strong candidates if you want a second example:** "who is governor of
ohio 2011" (37.4% rejected) and "what did st augustine do" (37.3% rejected) —
both show even more dramatic filtering, at the cost of being less immediately
relatable than the Nixon example.

**Live-demo script (suggested):**
1. Open the app, select the Nixon question from the sidebar.
2. Step 1–2: point at the question and the KG subgraph — "this is what GCR
   would search over, unfiltered."
3. Step 3 (TypeOracle gates): scroll to the rejected list — "these are real
   KG paths GCR would keep and ask the LLM to filter using its own judgment;
   TypeOracle removes them structurally, with a named reason."
4. Step 5: show the correct answer is still found through an admitted path —
   "filtering removed noise without removing the gold path, for this
   example."
5. Close the loop: "in aggregate across 1,628 questions this trade-off costs
   5.2 points of accuracy — which is the actual finding of the thesis."

**Backup plan:** record a 60–90 second screen capture of exactly this walk-
through in advance (in case of projector/Wi-Fi/laptop issues), and also put
the 2–3 key screenshots on a backup slide (see §3.1). Never rely on a live
demo working as your only path through this material.
