
class Solution {
    public int[] numberGame(int[] nums) {
        // 배열을 리스트로 변환 (수정 가능한 리스트)
        List<Integer> numsList = new ArrayList<>();
        for (int num : nums) {
            numsList.add(num);
        }

        // 리스트를 정렬합니다.
        Collections.sort(numsList);

        // 결과 배열을 담을 리스트 선언
        List<Integer> arr = new ArrayList<>();

        // 리스트의 길이가 0이 될 때까지 반복
        while (!numsList.isEmpty()) {
            // Alice가 최소값 제거
            int aliceMin = numsList.remove(0);

            // Bob이 최소값 제거
            int bobMin = numsList.remove(0);

            // Bob이 arr에 추가
            arr.add(bobMin);

            // Alice가 arr에 추가
            arr.add(aliceMin);
        }

        // 결과 리스트를 배열로 변환하여 반환
        return arr.stream().mapToInt(Integer::intValue).toArray();
    }

}
