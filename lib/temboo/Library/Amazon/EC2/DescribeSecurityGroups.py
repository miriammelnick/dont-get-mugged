
###############################################################################
#
# DescribeSecurityGroups
# Returns security group information associated with your AWS Account.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class DescribeSecurityGroups(Choreography):

    """
    Create a new instance of the DescribeSecurityGroups Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Amazon/EC2/DescribeSecurityGroups')


    def new_input_set(self):
        return DescribeSecurityGroupsInputSet()

    def _make_result_set(self, result, path):
        return DescribeSecurityGroupsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DescribeSecurityGroupsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the DescribeSecurityGroups
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class DescribeSecurityGroupsInputSet(InputSet):
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
        Set the value of the GroupName input for this choreography. ((optional, string) The name of the security group to return. Returns all groups if not specified.)
        """
        def set_GroupName(self, value):
            InputSet._set_input(self, 'GroupName', value)


"""
A ResultSet with methods tailored to the values returned by the DescribeSecurityGroups choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class DescribeSecurityGroupsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Amazon.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class DescribeSecurityGroupsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DescribeSecurityGroupsResultSet(response, path)
