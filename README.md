# Conditional Generative Adversarial Networks (CGAN) for Mobility Data Fusion

This code implements the paper, Kim et al. (2021). Imputing Qualitative Attributes for Trip Chains Extracted from Smart Card Data Using a Conditional Generative Adversarial Network. Transportation Research Part C. Under Review.

## Overview

This model aims to estimate the qualitative attributes of large-scale passively collected data (smart card data) using small-scale travel survey data, based on data fusion. The CGAN trains probability distribution of qualitative attributes given trip-chain attributes by mimicking the small-scale survey data..

## Getting Started

### Dependencies
* Python 3.6.10
* Tensorflow 2.4.1, Keras 2.4.3

### Components

#### Dataset
* 'Data' contains traffic crash data collected from six routes of interstate highway in California from 2006 to 2008.
* Based on the data, safety performance function (SPF) and continuous risk profile (CRP) were estimated and saved as separate files. For more details on calculating SPF and CRP, see [Kwon et al.(2013)](http://dx.doi.org/10.1016/j.aap.2012.10.019) and [Chung et al. (2009)](https://escholarship.org/uc/item/24m8j57d)

##### FatalCRP.R
* Step-by-step implementation of the proposed method is provided in a single file, including data preprocessing, modeling, evaluation, and visualization
* Refer the FatalCRP.html for a detailed description of the code  

## Notice
* Please refer to the full paper with this code for understanding the logic behind each process

## Authors

[@Eui-Jin Kim](https://sites.google.com/view/euijinkim)


## License

This project is licensed under the MIT License - see the LICENSE.md file for details

## Acknowledgments
* [Benchmark model](http://dx.doi.org/10.1016/j.aap.2012.10.019)
