
###############################################################################
#
# AddCSVData
# Transfer a csv file to add records to a specified group.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class AddCSVData(Choreography):

    """
    Create a new instance of the AddCSVData Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/ObadMobileMarketing/AddCSVData')


    def new_input_set(self):
        return AddCSVDataInputSet()

    def _make_result_set(self, result, path):
        return AddCSVDataResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AddCSVDataChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the AddCSVData
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class AddCSVDataInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((string) Private Key for 1 unique distributor - provided by Obad Mobile Marketing)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the ClientID input for this choreography. ((integer) Private Key for 1 unique customer to connect with - provided by Obad Mobile Marketing)
        """
        def set_ClientID(self, value):
            InputSet._set_input(self, 'ClientID', value)

        """
        Set the value of the Endpoint input for this choreography. ((string) The base URL for the server you want to access (i.e. http://10.10.10.1). Set this to the appropriate host for the demo sandbox or production.)
        """
        def set_Endpoint(self, value):
            InputSet._set_input(self, 'Endpoint', value)

        """
        Set the value of the GroupID input for this choreography. ((integer) Unique ID for the group you want to update)
        """
        def set_GroupID(self, value):
            InputSet._set_input(self, 'GroupID', value)

        """
        Set the value of the Type input for this choreography. ((string) Specify the desired item list (i.e. camp, coupon, usergroup, shopgroup, or coupongroup). Defaults to 'shopgroup'.)
        """
        def set_Type(self, value):
            InputSet._set_input(self, 'Type', value)

        """
        Set the value of the URLSource input for this choreography. ((string) The URL where you are hosting the CSV data (i.e. http://mybucket.s3.amazonaws.com/my_new_users.csv))
        """
        def set_URLSource(self, value):
            InputSet._set_input(self, 'URLSource', value)


"""
A ResultSet with methods tailored to the values returned by the AddCSVData choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class AddCSVDataResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Obad)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class AddCSVDataChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return AddCSVDataResultSet(response, path)
