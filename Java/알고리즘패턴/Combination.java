import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Combination {
    static int[] selected;
    static int[] datas;
    static int R;
    static int N;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        R = Integer.parseInt(st.nextToken());
        datas = new int[N];
        selected = new int[R];
        st = new StringTokenizer(br.readLine());
        for(int i=0; i<N; i++)
        {
            datas[i] = Integer.parseInt(st.nextToken());
        }


        combination(0, 0);

    }

    static void combination(int cnt, int start){
        if(cnt == R)
        {
            System.out.println(Arrays.toString(selected));
            return;
        }

        for(int i=start; i<N; i++)
        {
            selected[cnt] = datas[i];
            combination(cnt+1, i+1);
        }

    }
}
