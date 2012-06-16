
###############################################################################
#
# DescribeImageAttribute
# Retrieves information about an attribute of an AMI.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class DescribeImageAttribute(Choreography):

    """
    Create a new instance of the DescribeImageAttribute Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Amazon/EC2/DescribeImageAttribute')


    def new_input_set(self):
        return DescribeImageAttributeInputSet()

    def _make_result_set(self, result, path):
        return DescribeImageAttributeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DescribeImageAttributeChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the DescribeImageAttribute
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class DescribeImageAttributeInputSet(InputSet):
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
        Set the value of the Attribute input for this choreography. ((required, string) The AMI attribute to get. Valid Values are: description | kernel | ramdisk | launchPermission | productCodes | blockDeviceMapping.)
        """
        def set_Attribute(self, value):
            InputSet._set_input(self, 'Attribute', value)

        """
        Set the value of the ImageId input for this choreography. ((required, string) The AMI ID.)
        """
        def set_ImageId(self, value):
            InputSet._set_input(self, 'ImageId', value)


"""
A ResultSet with methods tailored to the values returned by the DescribeImageAttribute choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class DescribeImageAttributeResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Amazon.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class DescribeImageAttributeChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DescribeImageAttributeResultSet(response, path)
