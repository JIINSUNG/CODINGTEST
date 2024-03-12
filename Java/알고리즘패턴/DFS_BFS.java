import java.io.*;
import java.util.*;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class DFS_BFS {
    static int N;
    static int M;
    static int V;
    static boolean[] visited;
    static boolean[][] input;
    static Queue<Integer> queue;
    public static void main(String[] args)  throws IOException {
        //TIP Press <shortcut actionId="ShowIntentionActions"/> with your caret at the highlighted text
        // to see how IntelliJ IDEA suggests fixing it.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        V = Integer.parseInt(st.nextToken());
        input = new boolean[N+1][N+1];
        visited = new boolean[N+1];
        queue = new LinkedList<>();

        for(int i=0; i<M; i++)
        {
            st = new StringTokenizer(br.readLine());
            int v = Integer.parseInt(st.nextToken());
            int cv = Integer.parseInt(st.nextToken());

            input[cv][v] = input[v][cv] = true;
        }

        dfs(V);
        System.out.println();
        visited = new boolean[N+1];
        bfs(V);
    }

    static void dfs(int start)
    {
        visited[start] = true;
        System.out.print(start+" ");
        for(int i=0; i<N+1; i++)
        {
            if(input[start][i] && !visited[i])
            {
                dfs(i);
            }
        }
    }

    static void bfs(int start)
    {
        visited[start] = true;
        queue.add(start);

        while(!queue.isEmpty())
        {
            int v = queue.poll();
            System.out.print(v+" ");
            for(int i=0; i<N+1; i++)
            {
                if(input[v][i] && !visited[i])
                {
                    queue.add(i);
                    visited[i] = true;
                }
            }
        }

    }
}

