from typing import TypeAlias, List, Dict
from collections import OrderedDict
import json
from pathlib import Path

listOfStrings: TypeAlias = List[str]


class ClusterRuleJson:

    json_keys = [
        "name",
        "type_protein",
        "major_category",
        "minor_categories",
        "curation_category",
        "comment",
        "related",
        "cutoff",
        "neighborhood",
        "mandatory_hmm_list",
        "optional_hmm_list",
        "evil_hmm_list",
        "hmm_composition",
        "composition_rules",
    ]
    __slots__ = json_keys + ["json_template"]

    def __init__(
        self,
        name: str = None,
        type_protein: str = None,
        major_category: str = None,
        minor_categories: listOfStrings = None,
        curation_category=None,
        comment: str = None,
        related: listOfStrings = None,
        cutoff: int = None,
        neighborhood: int = None,
        mandatory_hmm_list: listOfStrings = None,
        optional_hmm_list: listOfStrings = None,
        evil_hmm_list: listOfStrings = None,
        hmm_composition: List[Dict] = None,
        composition_rules: Dict = None,
    ):

        self.name = name
        self.type_protein = type_protein  # TODO
        self.major_category = major_category
        self.minor_categories = minor_categories
        self.curation_category = curation_category
        self.comment = comment  # TODO
        self.related = related  # TODO
        self.cutoff = cutoff  # TODO
        self.neighborhood = neighborhood  # TODO
        self.mandatory_hmm_list = mandatory_hmm_list
        self.optional_hmm_list = optional_hmm_list
        self.evil_hmm_list = evil_hmm_list
        self.hmm_composition = hmm_composition
        self.composition_rules = composition_rules

    def validate_all(self):
        self.name = self.validate_clusterrule_name(self.name)
        self.type_protein = self.type_protein  # TODO
        self.major_category = self.validate_major_category(
            self.major_category, self.minor_categories
        )
        self.minor_categories = self.validate_minor_categories(self.minor_categories)
        self.curation_category = self.validate_curation_category(self.curation_category)
        self.comment = self.comment  # TODO
        self.related = self.related  # TODO
        self.cutoff = self.cutoff  # TODO
        self.neighborhood = self.neighborhood  # TODO
        self.mandatory_hmm_list = self.mandatory_hmm_list
        self.optional_hmm_list = self.optional_hmm_list
        self.evil_hmm_list = self.evil_hmm_list
        self.hmm_composition = self.hmm_composition
        self.composition_rules = self.composition_rules

    def build_json_dict(self):
        return OrderedDict({i: self.__getattribute__(i) for i in self.json_keys})

    def write_json(self, outpath: str = None):
        val_outpath = Path(outpath)
        if val_outpath.exists():
            raise FileExistsError(
                f"Cowardly not overwriting file: '{str(val_outpath)}'"
            )
        with open(val_outpath, "w") as outfile:
            json.dump(self.build_json_dict(), outfile)

    @staticmethod
    def validate_clusterrule_name(name: str = ""):
        min_char = 2
        max_char = 30
        if name is None or len(name) > max_char or len(name) < min_char:
            raise ValueError(
                f"'name' must be greater than {min_char} and less than {max_char} characters"
            )
        else:
            return name

    @staticmethod
    def validate_major_category(major_category, minor_categories):
        cat_opts = ["RIPP", "NRPS", "other"]
        if major_category not in cat_opts:
            raise ValueError(f"major_category must be one of: {cat_opts}")
        if major_category == "other" and minor_categories is [None]:
            raise ValueError(
                f"If major_category is 'other', minor_categories cannot be [None]"
            )
        return major_category

    @staticmethod
    def validate_minor_categories(minor_categories: listOfStrings = [None]):
        # TODO:
        return minor_categories

    @staticmethod
    def validate_curation_category(curation_category: str = None):
        cat_opts = ["manual", "automatic"]
        if curation_category not in cat_opts:
            raise ValueError(f"Curation category must be one of: {cat_opts}")
        else:
            return curation_category
