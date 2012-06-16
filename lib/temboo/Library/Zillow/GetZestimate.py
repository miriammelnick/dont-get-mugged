
###############################################################################
#
# GetZestimate
# Retrieve estimate information for a specified property.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetZestimate(Choreography):

    """
    Create a new instance of the GetZestimate Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Zillow/GetZestimate')


    def new_input_set(self):
        return GetZestimateInputSet()

    def _make_result_set(self, result, path):
        return GetZestimateResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetZestimateChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetZestimate
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetZestimateInputSet(InputSet):
        """
        Set the value of the RentEstimate input for this choreography. ((optional, boolean) Set to 1 (true) to enable. Defaults to 0 (false).)
        """
        def set_RentEstimate(self, value):
            InputSet._set_input(self, 'RentEstimate', value)

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
A ResultSet with methods tailored to the values returned by the GetZestimate choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetZestimateResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Zillow.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetZestimateChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetZestimateResultSet(response, path)
