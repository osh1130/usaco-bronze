#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;

#define MAXN 100000 // 定义数组的最大长度

int N; // 存储日志记录的数量
int A[MAXN]; // 存储每一天的计数器值

int main() {
    ifstream fin("taming.in");
    ofstream fout("taming.out");
    fin >> N; // 读取日志记录的数量
    for (int i = 0; i < N; i++) {
        fin >> A[i]; // 读取每一天的计数器值
    }

    // 检查第一天计数器是否大于0，如果是则日志不一致
    // if (A[0] > 0) {
    //     fout << -1 << '\n'; 
    //     return 0;
    // }
    A[0] = 0; // 将第一天的计数器设置为0

    int previousCount = -1; // 存储前一天的计数器值，初始化为-1
    int minBreakouts = 0; // 存储越狱次数的最小值，初始化为0

    // 从最后一天开始逆向扫描日志记录
    for (int i = N - 1; i >= 0; i--) {
        // 检查是否存在矛盾，即前一天的计数器值与当前记录不符
        // if (previousCount != -1 && A[i] != -1 && A[i] != previousCount) {
        //     fout << -1 << '\n'; // 出现矛盾，日志不一致
        //     return 0;
        // }

        // 更新 previousCount
        if (previousCount == -1) {
            previousCount = A[i]; 
        }

        // 填补缺失的计数器值
        if (A[i] == -1) {
            A[i] = previousCount; 
        }

        // 统计越狱次数
        if (A[i] == 0) {
            minBreakouts++; 
        }

        // 更新 previousCount
        if (previousCount > -1) {
            previousCount--; 
        }
    }

    // 填补缺失值后，再统计缺失条目
    int missingEntries = 0;
    for (int i = 0; i < N; i++) {
        if (A[i] == -1) {
            missingEntries++; 
        }
    }

    // 输出最小和最大越狱次数
    fout << minBreakouts << ' ' << minBreakouts + missingEntries << '\n'; 
    return 0;
}