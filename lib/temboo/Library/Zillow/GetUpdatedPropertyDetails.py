
###############################################################################
#
# GetUpdatedPropertyDetails
# Retrieve detailed property information that has been edited by the home's owner or agent.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetUpdatedPropertyDetails(Choreography):

    """
    Create a new instance of the GetUpdatedPropertyDetails Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Zillow/GetUpdatedPropertyDetails')


    def new_input_set(self):
        return GetUpdatedPropertyDetailsInputSet()

    def _make_result_set(self, result, path):
        return GetUpdatedPropertyDetailsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetUpdatedPropertyDetailsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetUpdatedPropertyDetails
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetUpdatedPropertyDetailsInputSet(InputSet):
        """
        Set the value of the ZPID input for this choreography. ((required, integer) Enter a Zillow Property ID for the property being queried.)
        """
        def set_ZPID(self, value):
            InputSet._set_input(self, 'ZPID', value)

        """
        Set the value of the ZWSID input for this choreography. ((required, string) Enter a Zillow Web Service Identifier (ZWS ID).)
        """
        def set_ZWSID(self, value):
            InputSet._set_input(self, 'ZWSID', value)


"""
A ResultSet with methods tailored to the values returned by the GetUpdatedPropertyDetails choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetUpdatedPropertyDetailsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Zillow.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetUpdatedPropertyDetailsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetUpdatedPropertyDetailsResultSet(response, path)
