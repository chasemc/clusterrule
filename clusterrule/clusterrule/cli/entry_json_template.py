import argparse
from pathlib import Path
import clusterrule.json_template as cr

parser = argparse.ArgumentParser(description="Create json from args")
parser.add_argument(
    "--outpath",
    metavar="filepath",
    help="input domtblout file. **Must** be an HMMSEARCH (**not** hmmscan) domtblout file ",
    required=True,
)
parser.add_argument(
    "--blank",
    metavar="boolean",
    help="Set to True to output a keys-only json file",
    required=False,
    default=False,
)


def main():
    args = parser.parse_args()
    if args.blank:
        cr_obj = cr.ClusterRuleJson()

        cr_obj.write_json(args.outpath)


if __name__ == "__main__":
    main()
