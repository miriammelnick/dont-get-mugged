
###############################################################################
#
# RegisterImage
# Registers a new AMI with Amazon EC2.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class RegisterImage(Choreography):

    """
    Create a new instance of the RegisterImage Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Amazon/EC2/RegisterImage')


    def new_input_set(self):
        return RegisterImageInputSet()

    def _make_result_set(self, result, path):
        return RegisterImageResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RegisterImageChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the RegisterImage
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class RegisterImageInputSet(InputSet):
        """
        Set the value of the AWSAccessKeyId input for this choreography. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        def set_AWSAccessKeyId(self, value):
            InputSet._set_input(self, 'AWSAccessKeyId', value)

        """
        Set the value of the AWSSecretKeyId input for this choreography. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        def set_AWSSecretKeyId(self, value):
            InputSet._set_input(self, 'AWSSecretKeyId', value)

        """
        Set the value of the Architecture input for this choreography. ((optional, string) The architecture of the image. Valid values are: i386 or x86_64. Defaults to i386.)
        """
        def set_Architecture(self, value):
            InputSet._set_input(self, 'Architecture', value)

        """
        Set the value of the DeleteOnTermination input for this choreography. ((optional, boolean) Whether the Amazon EBS volume is deleted on instance termination. Defaults to 1 (true).)
        """
        def set_DeleteOnTermination(self, value):
            InputSet._set_input(self, 'DeleteOnTermination', value)

        """
        Set the value of the Description input for this choreography. ((optional, string) The description of the AMI.)
        """
        def set_Description(self, value):
            InputSet._set_input(self, 'Description', value)

        """
        Set the value of the DeviceName input for this choreography. ((conditional, string) If registering an Amazon EBS-backed AMI from a snapshot, specify this input with the root device name (e.g., /dev/sda1, or xvda), and SnapshotId.)
        """
        def set_DeviceName(self, value):
            InputSet._set_input(self, 'DeviceName', value)

        """
        Set the value of the ImageLocation input for this choreography. ((conditional, string) Full path to your AMI manifest in Amazon S3 storage. Required if registering an Amazon-S3 backed AMI.)
        """
        def set_ImageLocation(self, value):
            InputSet._set_input(self, 'ImageLocation', value)

        """
        Set the value of the KernelId input for this choreography. ((optional, string) The ID of the kernel to select.)
        """
        def set_KernelId(self, value):
            InputSet._set_input(self, 'KernelId', value)

        """
        Set the value of the Name input for this choreography. ((required, string) A name for your AMI.)
        """
        def set_Name(self, value):
            InputSet._set_input(self, 'Name', value)

        """
        Set the value of the NoDevice input for this choreography. ((optional, boolean) Specifies that no device should be mapped. Defaults to 1 (true).)
        """
        def set_NoDevice(self, value):
            InputSet._set_input(self, 'NoDevice', value)

        """
        Set the value of the RamdiskId input for this choreography. ((optional, string) The ID of the RAM disk to select.)
        """
        def set_RamdiskId(self, value):
            InputSet._set_input(self, 'RamdiskId', value)

        """
        Set the value of the RootDeviceName input for this choreography. ((conditional, string) The root device name (e.g., /dev/sda1, or xvda). Required if registering an Amazon EBS-backed AMI.)
        """
        def set_RootDeviceName(self, value):
            InputSet._set_input(self, 'RootDeviceName', value)

        """
        Set the value of the SnapshotId input for this choreography. ((conditional, string) If registering an Amazon EBS-backed AMI from a snapshot, you must at least specify this input with the snapshot ID, and DeviceName with the root device name.)
        """
        def set_SnapshotId(self, value):
            InputSet._set_input(self, 'SnapshotId', value)

        """
        Set the value of the VirtualName input for this choreography. ((optional, string) The virtual device name.)
        """
        def set_VirtualName(self, value):
            InputSet._set_input(self, 'VirtualName', value)

        """
        Set the value of the VolumeSize input for this choreography. ((conditional, integer) The size of the volume, in GiBs. Required if you are not creating a volume from a snapshot.)
        """
        def set_VolumeSize(self, value):
            InputSet._set_input(self, 'VolumeSize', value)


"""
A ResultSet with methods tailored to the values returned by the RegisterImage choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class RegisterImageResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Amazon.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class RegisterImageChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RegisterImageResultSet(response, path)
