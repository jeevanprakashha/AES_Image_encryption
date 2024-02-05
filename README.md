# Image Encryption and Decryption using AES Algorithm with Email Verification

## Authors
- Jeevan Prakash1 (jeevanvitwork@gmail.com)
- Nikhil Sivakumar2 (nikhilsivakumar123@gmail.com)

## Table of Contents
- [Idea](#idea)
- [Scope](#scope)
- [Novelty](#novelty)
- [Comparative Statement](#comparative-statement)
- [Dataset](#dataset)
- [Test Bed](#test-bed)
- [Expected Result](#expected-result)
- [Architecture](#architecture)
- [Implementation](#implementation)
- [Results and Discussions](#results-and-discussions)
- [Website](#website)
- [References](#references)

## Idea
Our project introduces a simple yet effective method for encrypting and decrypting images using the AES algorithm, ensuring data security. We developed a website where users can securely encrypt their images. The process involves using the AES (Advanced Encryption Standard) algorithm, widely recognized for its strength and reliability in encryption. A unique feature of our system is embedding the user's email address within the encrypted image data. This embedding is crucial for the decryption phase, as it is tied to an additional security layer involving email verification.

## Scope
The scope of this project extends to anyone needing secure image handling – from individuals safeguarding personal photos to businesses protecting sensitive visual data. It's particularly useful in fields like healthcare, where patient confidentiality is vital, and in legal sectors where the security of photographic evidence is crucial. The simplicity and user-friendliness of our website make it accessible to users with varying levels of technical expertise, thus broadening its usability.

## Novelty
What sets our project apart is the integration of the user's email address into the encrypted image data. This integration is a novel approach in image encryption. During decryption, an OTP (One Time Password) is sent to this embedded email address, adding an extra layer of security. This means that to decrypt an image, one needs not only the correct decryption key but also access to the specific email account. This dual-security mechanism significantly enhances the overall safety of the encrypted images, ensuring that even if the encryption key is compromised, the image remains secure without access to the linked email.

## Comparative Statement
We compared our project with existing image encryption approaches and highlighted its unique features:

- **Unique Email Verification Feature:** Unlike other approaches that focus on complex algorithmic enhancements, our project incorporates the user's email within the encrypted data. This distinct feature of email-based OTP verification for decryption adds a personalized security dimension, differentiating it from purely technical modifications.

- **Emphasis on Simplicity and Accessibility:** While recent research trends towards integrating AES with other complex cryptographic systems, our project prioritizes ease of use. Our straightforward use of AES, complemented by an email OTP system, makes our project more accessible to a wider range of users, without requiring advanced technical expertise.

- **Focused Approach on AES and User Authentication:** Unlike other studies that diversify encryption techniques, our project maintains a commitment to the established AES standard, focusing on innovation in user authentication and key management. This approach offers a balance between high-grade security and a user-friendly experience, catering to the practical needs of users in a digital environment.

## Dataset
For our project "Image Encryption and Decryption Using AES Algorithm with Email Verification," we selected a diverse dataset consisting of various types of images. These images include a range of categories such as natural scenes, portraits, urban landscapes, and abstract art, ensuring a comprehensive test of the encryption system across different image complexities and color schemes. The dataset was chosen to represent typical image types that users might want to encrypt, thereby providing a realistic testing environment.

## Test Bed
Our test bed for this project was a controlled environment where both the encryption and decryption processes were rigorously tested. The setup included:

- A server hosting the web application, equipped to handle the AES encryption and decryption processes.
- Email service integration for OTP verification.
- A variety of devices and browsers to test the web application's compatibility and responsiveness.
- Software tools to measure the performance, security, and efficiency of the encryption and decryption processes.

## Expected Result
The expected result from running our encryption and decryption system on the test bed is to achieve secure and efficient image encryption and decryption, without significant loss of image quality or performance lag. Specifically, we anticipate:

- Successful encryption of all images in the dataset, with each resulting in a unique encrypted format.
- Smooth and secure email-based OTP verification process for decryption.
- Maintaining image integrity and quality post-decryption, ensuring that the decrypted image matches the original.
- Efficient performance in terms of encryption and decryption speed, suitable for practical use.
- High resistance to common cryptographic attacks, affirming the robustness of the AES algorithm complemented by our email verification system.

These results will demonstrate the effectiveness and reliability of our system in real-world scenarios, aligning with our goal of providing a user-friendly and secure image encryption service.

## Architecture
Our system follows a high-level design with Flask as the web framework for implementation. It consists of encryption and decryption processes, email OTP verification, and user interfaces for interaction. For a detailed low-level design, please refer to the code documentation.


## Implementation
The code implements a file encryption and decryption system using the AES encryption algorithm. It utilizes various algorithms and techniques, including:

- AES (Advanced Encryption Standard) for symmetric-key encryption.
- One-Time Password (OTP) generation for email-based verification.
- PKCS7 padding for data alignment.
- Random number generation for secure key and IV generation.

The code is structured as a Flask web application, providing a user-friendly interface for encryption and decryption. Users can upload an image for encryption and provide an email address. After encryption, a download link is provided for the user to retrieve the encrypted file. During decryption, users must enter the OTP sent to their email for verification.

For a detailed explanation of the implementation, please refer to the code documentation.

## Results and Discussions
The code implements a secure image encryption and decryption system using the AES algorithm. It provides the following results:

- Encryption: The code produces an encrypted file with the '.enc' extension. This file contains the ciphertext and the initialization vector (IV) required for decryption.

- Decryption: Upon successful decryption using the correct OTP and key, the code provides the original file in its decrypted form.

The code was tested in a controlled environment to ensure security, performance, and user-friendliness. It successfully achieves the goals of secure image handling with email-based OTP verification.

## Website
The web application provides a user-friendly interface for image encryption and decryption. It consists of the following pages:

1. **Selection Page:** Users are presented with options to either encrypt or decrypt images.

2. **Encrypt Page:** Users can upload an image and provide their email for encryption. After processing, they receive a ZIP file containing the encrypted image and key.

3. **Sample Encryption:** Demonstrates the encryption process with a sample image.

4. **Decryption Page:** Users upload the encrypted ZIP file and provide the decryption key. They also receive an OTP for email verification.

5. **Sample Decryption:** Demonstrates the decryption process with a sample encrypted image.

The website's user interface is intuitive and straightforward, making it accessible to users with varying levels of technical expertise.

## References
List of references to related research papers and materials used in the project:

1. Zeghid, M., Machhout, M., Khriji, L., Baganne, A. and Tourki, R., 2007. A modified AES based algorithm for image encryption. International Journal of Computer and Information Engineering, 1(3), pp.745-750.

2. Subramanyan, B., Chhabria, V.M. and Babu, T.S., 2011, February. Image encryption based on AES key expansion. In 2011 Second International Conference on Emerging Applications of Information Technology (pp. 217-220). IEEE.

3. Singh, A., Agarwal, P. and Chand, M., 2019, April. Image encryption and analysis using dynamic AES. In 2019 5th international conference on optimization and applications (ICOA) (pp. 1-6). IEEE.

4. Alsaffar, D.M., Almutiri, A.S., Alqahtani, B., Alamri, R.M., Alqahtani, H.F., Alqahtani, N.N. and Ali, A.A., 2020, March. Image encryption based on AES and RSA algorithms. In 2020 3rd International Conference on Computer Applications & Information Security (ICCAIS) (pp. 1-5). IEEE.

5. Ghoradkar, S. and Shinde, A., 2015. Review on image encryption and decryption using AES algorithm. International Journal of Computer Applications, 975, p.8887.

6. Msolli, A., Helali, A. and Maaref, H., 2016, March. Image encryption with the AES algorithm in wireless sensor network. In 2016 2nd International Conference on Advanced Technologies for Signal and Image Processing (ATSIP) (pp. 41-45). IEEE.

7. Bashir, A., Hasan, A.S.B. and Almangush, H., 2012. A new image encryption approach using the integration of a shifting technique and the AES algorithm. Int. J. Comput. Appl, 975, p.8887.

8. Asim, M. and Jeoti, V., 2007, February. On image encryption: Comparison between AES and a novel chaotic encryption scheme. In 2007 International Conference on Signal Processing, Communications and Networking (pp. 65-69). IEEE.

9. Shakir, H.R., 2019. An image encryption method based on selective AES coding of wavelet transform and chaotic pixel shuffling. Multimedia Tools and Applications, 78(18), pp.26073-26087.

10. Kamali, S.H., Shakerian, R., Hedayati, M. and Rahmani, M., 2010, August. A new modified version of advanced encryption standard based algorithm for image encryption. In 2010 international conference on electronics and information engineering (Vol. 1, pp. V1-141). IEEE.

## License
This project is licensed under the [MIT License](LICENSE).
