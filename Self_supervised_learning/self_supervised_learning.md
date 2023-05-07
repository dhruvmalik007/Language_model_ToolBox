## Self supervise training & deployment process

following the notes of the yann le cun's seminal paper "cookbook about SSL"

## credits:

- [cookbook in self supervised learning]()
- [explaining 101 techniques](https://docs.lightly.ai/self-supervised-learning/getting_started/advanced.html). 
    
    
    
# WIP:    
- [ ] using lightly.ai package for doing the necessary transformations (for the CV tasks)
- [ ] building your own package interoperable on both torch / tf implementations , and then create the machine ;earning lifecycle. 



## 1. Training & Deployment steps: 

- data augmentation pipeline: 
    - SSL methods like [image gpt paper](https://github.com/openai/image-gpt) defines the data augmentation techniques   like using different crpos for given +ve / -ve view, collerJitter & greyscale operation.
        - removes the need of handcrafted data aug techniques.  

    - Multicrop technique: Coalescing the different cropping of the image by superimposing the various smaller versions of image into larger one. 
        - various techniques : [SwAV](https://paperswithcode.com/method/swav) mitigate the memory cost reduction with quarter increase in the training time but significant performance boost. 

    - [Adding Projector](Bordes-etal): doing fuzzing changes in the major DNN's  . this in the terms of transfer learning is important to take into consideration in order to differentiate the training task from the downstream tas.
        - it uses Guillotine Regularization for probing the repreentation

- [training SSL without projectors](https://github.com/facebookresearch/luckmatters/tree/main/ssl). 
    - using the contrastive method, DirectCLR that uses the various other techniques like InfoNCE based SimCLR objective on subvectors. 
        - [InfoNCE](): InfoMax Contrastive learning, is the function used in SSL that 
            - generates representations of the various augmented views of same input, which then insures that model captures the more meaningful features of input.
        - [SimCLR](): Simple Constrastive learning, uses the InfoNCE loss output to learn the representations of the input data.
        - [MoCo-V3](): Memory Augmented Constrastive learning for vision: is the ssl method for learning representations of the image data.
            -  its improved implementation of the SimCLR, where it introduces the dynamic Queue of negative samples , which are updated during training to improve quality of the various examples used in the constrastive loss.
     

- Some terminologies 
    - [backbone](): is the CNN architecture that is used for extracting features from input images / details concerning the model on which its trained. 


- Understanding SSL implementation in Vision Transformers: 
    - MIM approach : mutual information maximization is the ssl technique for learning representations for image data. the aim here is to maximize the mutual information between the two sets of representations of same input. 
    - iBOT model : uses ViT for being both the teacher and pupil in distilling further the results of the MiM. 


## Other use cases (beyond classification of images):
- even for object detection and semantic segmentation where models have to learn more complex segmentations. 


## Model evluations:
- currently there are only techniques available for their evaluation for the vision models 
    - Traditional unsupervised techniques : KNN, mlp etc
    - Full Fine Tuning:
    - Visual Representation using RCDM evaluation 
        - Stands for Relative Contrastive Divergence Minimization, its an evaluation of quality of representations learned by SSL models for image, by quantifying the relative similarity between the different images in the dataset.
    - RankMe algorithm: Generating the effective 
        



## Training Evaluations:
-  Via distributed training: using the libraries like [FairScale's](https://github.com/facebookresearch/fairscale) Fully Shared Data paralel & Distributed Data Parallel. 
-  Using [FFCV library](https://github.com/facebookresearch/FFCV-SSL) that is the fork of [ffcv.io]() version of the libraries but for the SSL workflows.
- [XFormers]().
- [Apex]().

## extending SSL in other category of data (apart from images):

- Not easily able to apply for audio, text and tabular data: because of the fact that contrastive learning in audio and text systems and data augmentation is unstable to train model and get a optimal increase of performance. 
    - image transformations like horizontal flipping, pixelation and color encoding does not effectuate major changes while it can render the audio / text data illisible (anapohra resolution in the NLP is the main example).

    - Also for the Text data, most of the text data is being generated with the context of the reconstruction method rather than constrastive method. 


- Tabular data augmentation is already well studies : mixup and conversion of the missing and corrupted values 
    - TODO: how this can be better amplified with the generative AI: based on the context of the given sensor readings or cenus data, based on the context of the given value, we can assign a given values based on the other parameters (using prompts). 

    - CutMix and Mixup techniques 



### reinforment learning (& specially RLHF) with SSL: 
- applying on the video: considering as state change of actions, there can be application of the contrastive learning to match the current state representation and next time step representation. 
- various benchmark models:
    - CURL: Representations for Reinforcement Learning, defined by Kumar etal(2020) is useful for understandinf representations of state space in the RL problem.
        - it uses constrastive learning to understand the transitions of the enviornment. 
        - consist of encoder & predictor network: the encoder determines the representation of state & the predictor for predicting the reward obtaioned by taking an action in the given state. 
    -  [BYOL]() : Bootstrap your own latent is the SSL method for learning the useful; representations of data, based on the context of deep neural networks
    -  [Barlow twins]()
    - [Efficient Zero]() is the most efficient method, which takes the inspiration from the deepmind benchmark model MuZero. 
    - [VIP and R3M models trained on Ego4D dataset]()

## Adding multiple Modalities into SSL training: 

1. some of the multimoal vision-language model already using SSL:
    - [Contrastive Language Image Pre-training(CLIP)] : uses transformer based model that uses constrastive learning joint representations of image & text.  it uses the contrastive learning pre training objective. it does random cropping and jittering to do data augmentations
    - [ALIGN](): its developed on transformer based architecture with separate encoders for images / text. its architecture consist of seq of CNN along with tarnsformer end. unlike CLIP, its only subtractive in nature and does random cropping for dataset augmentation. 


### showdown of CNN's vs ViT (TODO: and also with capsnet):
- ViT are more superior in the localization and contextual information from their features.
    - This information comes naturally in the patchwise features.

### learning localization features without annotations:
    - done by modifying the SSL routines specifically to enhance the localization in their features. 
    - some of the models in this category
        - DenseCL: matches most similar pixelwise features extracted from augmented samples and then detect the various relations in the image (for instance  there are various changes in the object positions, details etc).
    





## Mermaid based diagrams defining the benchmark of the various techniques: 

TODO:

