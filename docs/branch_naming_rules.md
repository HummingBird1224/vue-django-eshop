# ブランチ命名規則


### 基本
- ケバブケース 
- `-`以外の記号は使わない（半角の英数字のみ）

### prefix
| prefix | rules |
|--------|-------|
| wip    |   Works in progress. いつ終わるかわからないもの |
| feat   |   Feature. 開発中の新機能 | 
| bug    |   Bug fix. バグ修正 |
| junk   |   Throwaway branch. 試しに作ってみる機能等いつ捨ててもいいもの |

### issue id (今はなし)
タスク管理ツールのissue idをブランチ名の最後につける


### Example
- `feat/new-design-tool-13124412`


### Future Updates
- チームの人数が増えてきたらfeatureごとにさらにprefixを決めるかも
    - `feat/new-design-tool/3d-modeling-2312312`
- prefixも増えるかも
