import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Subset {
    static int N;
    static int[] datas;
    static boolean[] selected;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        datas = new int[N];
        selected = new boolean[N];

        for (int i=0; i<N; i++)
        {
            datas[i] = Integer.parseInt(br.readLine());
        }

        subset(0,0);

    }
    static void subset(int cnt, int flag)
    {
        if(cnt == N)
        {
            for(int i=0; i<N; i++)
            {
                if((flag & 1<<i)!=0)
                {
                    System.out.print(datas[i]+" ");
                }
            }
            System.out.println();
            return;
        }

        subset(cnt+1, flag | 1<<cnt);
        subset(cnt+1, flag);
    }
}
