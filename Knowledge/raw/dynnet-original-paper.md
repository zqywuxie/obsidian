## Abstract

Single-cell RNA sequencing has revolutionized our ability to dissect cellular heterogeneity and study cell fate mechanisms, yet inferring stochastic dynamics from static snapshots remains a fundamental challenge. Current approaches face a critical trade-off: mechanistic models impose rigid assumptions limiting biological realism, while data-driven methods sacrifice interpretability for deeper mechanistic explorations. Here, we present DynNet, a deep learning method that integrates Neural ODEs with biophysical models and prior knowledge of gene expression dynamics. DynNet learns the stochastic dynamics of gene regulatory systems for cell fate decisions. Benchmarking on synthetic data shows DynNet’s ability to infer stable cell states, reconstruct dynamical trajectories, and characterize multi-stable cell fate transitions. Using hepatocyte differentiation data, DynNet demonstrates its capability to infer developmental trajectory and the underlying cell fate landscape, revealing the stability and transition probabilities among distinct cell states. Applied to Epithelial-mesenchymal transition (EMT) data, DynNet further captures critical gene regulations and transition paths during EMT.

## Funding

C.L. is supported by the National Natural Science Foundation of China (Grant no. 12171102) and the National Key R&D Program of China (Grant no. 2019YFA0709502).

## Ethics declarations

### Competing interests

The authors declare no competing interests.

## Additional information

**Publisher’s note** Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## Source data

### Source Data (download XLSX )

## Rights and permissions

**Open Access** This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material. You do not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit [http://creativecommons.org/licenses/by-nc-nd/4.0/](http://creativecommons.org/licenses/by-nc-nd/4.0/).

[^1]: Institute of Science and Technology for Brain-Inspired Intelligence, Fudan University, Shanghai, China

Jingyu Dou, Feng Chen & Chunhe Li

[^2]: Shanghai Center for Mathematical Sciences, Fudan University, Shanghai, China

Jingyu Dou, Wentao Lyu & Chunhe Li

[^3]: Department of Mathematics and Department of Developmental and Cell Biology, University of California, Irvine, Irvine, CA, USA

Qing Nie

[^4]: School of Mathematical Sciences, Center for Applied Mathematics, Shanghai Key Laboratory for Contemporary Applied Mathematics, and MOE Frontiers Center for Brain Science, Fudan University, Shanghai, China

Chunhe Li