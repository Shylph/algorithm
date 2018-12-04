package jmbook_study.bitmask_16;

public class BitMask {
    public static void main(String[] argv) {
        System.out.println("공집합 : " + "0");
        System.out.println("꽉찬 집합(5개 기준) : " + Integer.toBinaryString((1 << 5) -1) );
        int set1 = 0;
        set1 |= (1 << 2);
        System.out.println("3번째에 원소 추가 : " + Integer.toBinaryString(set1));

        System.out.println("원소 포함 여부 확인");
        if((set1 & (1 << 2)) == (1 << 2)) //연산 결과는 0 or (1<<2)
            System.out.println("\t3번째 원소 포함 됨");

        System.out.println("3번째 원소 삭제");
        set1 &= ~(1 << 2);
        System.out.println("\t삭제 결과 : " + Integer.toBinaryString(set1));

        System.out.println("3번째 원소 토글");
        set1 ^= (1 << 2);
        System.out.println("\t토글 결과 : " + Integer.toBinaryString(set1));

        int set2 = (1 << 1);

        System.out.println("합 집합" + Integer.toBinaryString(set1 | set2));
        System.out.println("교 집합" + Integer.toBinaryString(set1 & set2));
        System.out.println("차 집합" + Integer.toBinaryString(set1 & ~set2));
        System.out.println("1,2 중 하나만 포함된 집합" + Integer.toBinaryString(set1 ^ set2));


        System.out.println("집합 크기 구하기 : " + Integer.bitCount(set1));
        System.out.println("최소 원소 찾기(=최하위 비트 위치) : " + Integer.numberOfTrailingZeros(set1));
        System.out.println("최소 원소의 값 : " + (set1 & -set1));
        System.out.println("최소 원소 지우기");
        set1 &= (set1 - 1);
        System.out.println("\t결과 : " + set1);

        set1 |= 1 + (1<<2) + (1<<4);
        System.out.println("공집합을 제외한 모든 부분 집합 순회");
        for(int subset = set1;subset != 0;subset = ((subset-1) & set1)){
            System.out.println(Integer.toBinaryString(subset));
        }

    }


}
