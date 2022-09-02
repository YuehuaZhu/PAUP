# PAUP
This is the official pytorch code for the SIGIR 2022 paper "[Progressive Self-Attention Network with Unsymmetrical Positional Encoding for Sequential Recommendation](https://scholar.archive.org/work/b2eo45jxn5cmhg263ilwps4o7m/access/wayback/https://dl.acm.org/doi/pdf/10.1145/3477495.3531800)". In this paper, to simultaneously capture the long-term and short-term dependencies among items (see the left figure below), we propose a novel convolutional self-attention network (see the right figure below), namely [PAUP](https://github.com/YuehuaZhu/PAUP/blob/master/recbole/model/sequential_recommender/paup.py), which helps progressively extract the sequential patterns. Our 5-min video talk about this work is available in the [*Supplemental Material*](https://dl.acm.org/doi/10.1145/3477495.3531800).

<img src="https://github.com/YuehuaZhu/PAUP/blob/master/pic/illustration.png" width="400" alt="illustration"/><img src="https://github.com/YuehuaZhu/PAUP/blob/master/pic/framework.png" width="400" alt="pipline"/>





## Installation
We mainly recommend the following important dependencies.
- python==3.7.7
- pytorch==1.3.1


## Datasets
We use three real-world benchmark datasets, including Yelp, Amazon Books and ML-1M. The details about full version of these datasets are on [RecSysDatasets](https://github.com/RUCAIBox/RecSysDatasets). Download three well-processed benchmarks from [RecSysDatasets](https://github.com/RUCAIBox/RecSysDatasets), and put them in .\dataset.

## Quick Guide
Here, we already download the dataset ml-1m, and the PAUP model can be trained by script run_recbole.py, with a simple call given here:
```bash
python run_recbole.py 
```
Thanks the great work of  [LightSANs](https://github.com/RUCAIBox/LightSANs). We adopt LightSANs as our baseline model, and we keep most parameter settings to ensure fair comparsions. Therefore, we mainly tune the parameter "m" and "k1" in "PAUP.yaml" to achieve better performance. Note that we encourage more experimentations on parameter m and k_1, which may resulte in better overall performance than that described in the paper.

## Acknowledgements
Our work is inspired from many recent efforts in various Transformer-based methods including: [LightSANs](https://github.com/RUCAIBox/LightSANs), [Synthesizer](https://github.com/leaderj1001/Synthesizer-Rethinking-Self-Attention-Transformer-Models), [LinTrans](https://github.com/idiap/fast-transformers), [Performer](https://github.com/lucidrains/performer-pytorch), [Linformer](https://github.com/lucidrains/linformer), [BERT4Rec](https://github.com/FeiSun/BERT4Rec), [SASRec](https://github.com/kang205/SASRec). Many thanks for their great work!

## Citation

If you find our paper or this project helps your research, please kindly consider citing our work via:
```
@inproceedings{Zhu2022PAUP,
  title={Progressive Self-Attention Network with Unsymmetrical Positional Encoding for Sequential Recommendation},
  author={Yuehua Zhu, Bo Huang, Shaohua Jiang, Muli Yang, Yanhua Yang and Wenliang Zhong},
  booktitle={SIGIR},
  year={2022}
}
```

 
