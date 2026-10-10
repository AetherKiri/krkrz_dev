# Math

特殊运算

## 成员列表

### 方法

- [octetVectorSum](#octetvectorsum)

---

### octetVectorSum

方法

**参数**

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `a` | `&nbsp;` |  |
| `b` | `void` |  |

**返回值**

[ Σ(ai*bi), Σ(ai-bi)^2, Σai^2, Σbi^2, Σai, Σbi, Σ(ai!=bi) ]，或当 bi===void 时为 [ 0, Σai^2, Σai^2, 0, Σai, 0, Σ(ai!=0) ]

**说明**

将 octet 视为向量进行运算

内积为 r[0]，欧几里得距离为 Math.sqrt(r[1])，余弦相似度为 r[0]/(sqrt(r[2])*sqrt(r[3]))

---
