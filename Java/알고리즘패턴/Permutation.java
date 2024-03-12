import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Permutation {
    static int N, R;
    static int[] datas;
    static int[] selected;
    static boolean[] visited;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        R = Integer.parseInt(st.nextToken());
        datas = new int[N];
        selected = new int[R];
        visited = new boolean[N];
        st = new StringTokenizer(br.readLine());
        for(int i=0; i<N; i++)
        {
            datas[i] = Integer.parseInt(st.nextToken());
        }

        permutation(0);
    }

    static void permutation(int cnt)
    {
        if(cnt == R)
        {
            System.out.println(Arrays.toString(selected));
            return;
        }

        for(int i=0; i<N; i++)
        {
            if(visited[i])
                continue;
            visited[i] = true;
            selected[cnt] = datas[i];
            permutation(cnt+1);
            visited[i] = false;
        }
    }
}
