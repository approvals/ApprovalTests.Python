from typing import Sequence, Any, Dict

from approvaltests.pairwise_combinations import get_best_covering_pairs


def get_key(in1: Any, in2: Any) -> str:
    return f"({in1},{in2})"


def add_pair(in1: Any, in2:Any, all_pairs_with_index: Dict[str,int]) -> None:
    key = get_key(in1, in2)
    all_pairs_with_index.setdefault(key, len(all_pairs_with_index))


def get_all_pairs_count(inputs: Sequence[Sequence[Any]])-> Dict[str, int]:
    cases = get_best_covering_pairs(inputs)
    pairCount = {}
    for params in cases:
        for i1 in range(len(inputs)-1):
            for i2 in range(i1+1, len(inputs)):
                in1 = params[i1]
                in2 = params[i2]
                add_pair(in1, in2, pairCount)
    return pairCount


def assert_all_pairs_present_between_lists(input1:Sequence[Any], input2:Sequence[Any], all_pairs_with_index: Dict[str, int])-> None:
    for i1 in input1:
        for i2 in input2:
           key = get_key(i1, i2)
           if not key in all_pairs_with_index.keys():
               raise Exception(f"could not find pair {key}")


def assert_all_pairs_present(all_pairs_with_index: Dict[str, int], inputs: Sequence[Sequence[Any]]) -> None :
    for i1 in range(len(inputs) - 1):
        for i2 in range(i1 + 1, len(inputs)):
            assert_all_pairs_present_between_lists(inputs[i1], inputs[i2], all_pairs_with_index)


def assert_pairwise_combinations(inputs: Sequence[Sequence[Any]]) -> None:
    all_pairs_with_index = get_all_pairs_count(inputs)
    assert_all_pairs_present(all_pairs_with_index, inputs)

    #allPairCombinationCount = calculateAllPairCombinationCount(inputs)
    # assertEquals(121, allPairCombinationCount)
    #assertEquals(allPairCombinationCount, pairCount.size())
    
def test_pair_properties() -> None:
      input1 = [112, 111, 113, 114, 115]
      input2 = [221, 222, 223, 224]
      input3 = [331, 332, 333, 334, 335]
      input4 = [441, 442, 443, 444]
      assert_pairwise_combinations([input1, input2, input3, input4])

