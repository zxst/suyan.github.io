---
layout: post
title: Overview of drug discovery
category: 新药研发
tag: Drug Discovery
---

### Drug discovery pipeline
1.  Target selection and validation
2.  Hit finding
3.  Lead optimization
4.  Toxicity handling
5.  Animal model testing
6.  Phase I/II/III clinical testing  

### 1.Target selection
*  **Target driven drug discovery**
*  Phenotypic drug discovery
*  Hybridizing the strengths of phenotypic and target driven discovery

### 2.Target validation
 Choosing a challenging target is usually a bad idea unless there’s some new enabling biochemical technology that enables this targeting.
 * This process is largely one of guesswork, and tends to rely upon experienced biologists’ intuitions.这个过程主要靠猜测，而且往往依靠经验的生物学家的直觉。

### 3.Hit finding
The process of finding a hit might be significantly different depending on the type of drug you’d like to design. The two major types of drugs are small molecules`(designed and created by chemists)` and biologics`(often antibodies)`.
* **Small molecules**
  * Search public databases or patent literature. More often than not, some compounds will be available
  * `(HTS)`High throughput screening assay
* **Antibodies**
  * Phage display, which expresses the desired target on the surface of a bacteriophage (a type of virus) and uses it to select amongst various antibody choices.噬菌体展示，其表达噬菌体表面上所需的靶标（一种病毒），并用它来选择各种抗体。
* **Computional in hit finding**
  * `virtual screening` speed up the hit finding process
  * Computational methods are almost exclusively used for small molecule,几乎只对小分子有用，但随着计算方法的发展，对大分子的支持将指年可待。

### Lead optimization
 Idea is to modify the hit molecule to tightly interact with the desired target biomolecule,the medicinal chemists will teratively modify the structure of the hit molecule until it binds tightly with the target biomolecule. `Can be reliably contracted out to external labs.`
 * **Computional in Lead optimization**  
 Schrodinger’s FEP suite has gained some traction amongst pharmaceutical companies for lead optimization.薛定谔的FEP套件在制药公司中获得了使用，用于优化lead compound.



### Toxicity testing
Testing whether the compound is safe for human ingestion. `Involves ADME (absorption, distribution, metabolism, and excretion)` property characterization. Standard experiments `(hERG, CYP450 inhibition test)` for small molecules that measure whether there exist negative interactions with unsuitable biological systems.
* **Computional in Toxicity testing**  
Tox21 challenge for computational toxicology (won by deep learning) raised hope that deep learning methods could advance toxicity testing.
---
`All of the computational methods mentioned above  are working in progress, with partial progress, but no definitive advances yet.`
