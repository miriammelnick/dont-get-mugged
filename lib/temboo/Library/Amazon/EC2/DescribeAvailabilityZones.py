
###############################################################################
#
# DescribeAvailabilityZones
# Returns Availability Zones that are available for your EC2 account.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class DescribeAvailabilityZones(Choreography):

    """
    Create a new instance of the DescribeAvailabilityZones Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Amazon/EC2/DescribeAvailabilityZones')


    def new_input_set(self):
        return DescribeAvailabilityZonesInputSet()

    def _make_result_set(self, result, path):
        return DescribeAvailabilityZonesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DescribeAvailabilityZonesChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the DescribeAvailabilityZones
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class DescribeAvailabilityZonesInputSet(InputSet):
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
A ResultSet with methods tailored to the values returned by the DescribeAvailabilityZones choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class DescribeAvailabilityZonesResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Amazon.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class DescribeAvailabilityZonesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DescribeAvailabilityZonesResultSet(response, path)
