# PAUP
Official PyTorch code for the Sigri 2022 poster paper "Progressive Self-Attention Network with Unsymmetrical Positional Encoding for Sequential Recommendation". In this paper, we mainly propose a novel convolution-based self-attention network, namely PAUP, which is simple to implement. The pipeline of PAUP is as shown below.





## Installation
We recommend the following dependencies.
- python==3.7.7
- pytorch==1.3.1


## Datasets
1. We use three real-world benchmark datasets, including Yelp, Amazon Books and ML-1M. The details about full version of these datasets are on [RecSysDatasets](https://github.com/RUCAIBox/RecSysDatasets). Download three well-processed benchmarks from [RecSysDatasets](https://github.com/RUCAIBox/RecSysDatasets), and put them in .\dataset.

## Quick Guide
Here, we already download the dataset ml-1m, and the PAUP model can be trained by script run_recbole.py, with a simple call given here:
```bash
python run_recbole.py 
```
Thanks the great work of  [LightSANs](https://github.com/RUCAIBox/LightSANs). We adopt LightSANs as our baseline model, and we keep most parameter settings to ensure fair comparsions. Therefore, we mainly tune the parameter "m" and "k1" in "PAUP.yaml" to achieve better performance. Note that we encourage more experimentations on parameter m and parameter k_1, which may resulte in better overall performance than that described in the paper.

## Citation

If you find our paper or this project helps your research, please kindly consider citing our work via:
```
@inproceedings{Zhu2022PAUP,
  title={Progressive Self-Attention Network with Unsymmetrical Positional Encoding for Sequential Recommendation},
  author={Yuehua Zhu, Bo Huang, Shaohua Jiang, Muli Yang, Yanhua Yang and Wenliang Zhong},
  booktitle={Sigri},
  year={2022}
}
```

 
