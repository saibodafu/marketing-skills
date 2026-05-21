#!/usr/bin/env python3
"""Generate a simple markdown campaign brief from command-line inputs."""

from __future__ import annotations

import argparse
from textwrap import dedent


def build_brief(args: argparse.Namespace) -> str:
    proof_points = args.proof or "Assumption: proof points need to be supplied by the user."
    cta = args.cta or "Assumption: confirm the desired next action before final use."
    measurement = args.measurement or "Assumption: use channel-specific engagement and conversion metrics."

    return dedent(
        f"""
        ## Campaign Brief

        **Campaign Name:** {args.campaign}
        **Objective:** {args.objective}
        **Audience:** {args.audience}
        **Offer:** {args.offer}
        **Primary Channel:** {args.channel}

        ### Core Insight
        The audience needs a clear reason to care now: connect their current pressure to the specific value of {args.offer}.

        ### Message Strategy
        - Main message: {args.offer} helps {args.audience} make progress on {args.objective}.
        - Supporting proof: {proof_points}
        - Tone: Direct, useful, and commercially grounded.

        ### Creative Direction
        - Visual direction: Show the product or outcome clearly, with minimal decorative clutter.
        - Copy direction: Lead with the business problem, then present the offer as the practical answer.
        - Content modules: Problem, offer, proof, use case, CTA.

        ### Channel Execution
        - Format: Build for {args.channel}.
        - CTA: {cta}
        - Measurement: {measurement}

        ### Assumptions
        - Missing fields were filled with conservative placeholders.
        - Replace assumptions with confirmed business, audience, and channel data before production.
        """
    ).strip()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build a markdown marketing campaign brief.")
    parser.add_argument("--campaign", required=True, help="Campaign name.")
    parser.add_argument("--audience", required=True, help="Target audience.")
    parser.add_argument("--offer", required=True, help="Product or offer.")
    parser.add_argument("--objective", required=True, help="Business objective.")
    parser.add_argument("--channel", required=True, help="Primary channel.")
    parser.add_argument("--proof", help="Key proof points.")
    parser.add_argument("--cta", help="Call to action.")
    parser.add_argument("--measurement", help="Primary measurement approach.")
    return parser.parse_args()


def main() -> None:
    print(build_brief(parse_args()))


if __name__ == "__main__":
    main()
