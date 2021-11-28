# How To Verify Binary Blobs

<!-- toc -->
## Contents

  * [Examples](#examples)
    * [Approving images](#approving-images)
    * [Approving NumPy arrays](#approving-numpy-arrays)<!-- endToc -->

Using the `verify_binary` function, you can also check binary data blobs. For instance, you could check that your 
program produces correct image frames. Another example would be approving and checking numpy arrays in scientific 
applications.

## Examples

### Approving images
In this example, you can see how `verify_binary` is used to approve rendered images.

<!-- snippet: verify_binary_image -->
<a id='snippet-verify_binary_image'></a>
```py
name = "icon.png"
filename = get_adjacent_file(name)
with open(filename, mode='rb') as f:
    verify_binary(f.read(),".png")
```
<sup><a href='/tests/test_verify.py#L153-L158' title='Snippet source file'>snippet source</a> | <a href='#snippet-verify_binary_image' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

Which will produce

![Approved image](../../tests/approved_files/VerifyTests.test_verify_file_binary_file.approved.png)

### Approving NumPy arrays
This more detailed example demonstrates how you could use `verify_binary` to approve NumPy arrays. 

It uses serializers instead of dumping the binary blob directly to disk. In this case, the serialization provided by NumPy is used.

snippet: verify_numpy_array

It also shows the use of a custom reporter, which uses the NumPy testing features to produce a well-formatted error report highlighting the differences between arrays.

snippet: numpy_custom_reporter
