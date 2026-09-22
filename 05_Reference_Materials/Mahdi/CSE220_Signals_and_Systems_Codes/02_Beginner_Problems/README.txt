Beginner Set - Signals and Their Properties (10 problems)
=========================================================
templates/   P01..P10 - starter files. Implement only the functions under
             "ANSWER IMPLEMENTATION"; base signals + plotting helpers are given.
solutions/   P01..P10 - reference solutions (each tested; run to see figures).

Run:  python3 templates/P01_template.py     (raises NotImplementedError until filled)
      python3 solutions/P01_solution.py

Order (each builds toward the advanced set):
  01 basic signals        -> vocabulary for everything
  02 amplitude & offset   -> transform amplitude step (adv P02/P10)
  03 piecewise masks      -> prototype pulses (adv P10)
  04 add & multiply       -> echo sums / modulation (adv P05)
  05 DT step/impulse/rect -> discrete-time basics
  06 time shift (interp)  -> shift step of transforms (adv P02/P05/P10)
  07 downsampling         -> time scaling (adv P06)
  08 DT energy            -> energy signals (adv P01/P04)
  09 periodic power       -> power of periodic signals (adv P08)
  10 sampling a sinusoid  -> CT vs DT energy (adv P09)

Requires: python3, numpy, matplotlib.
