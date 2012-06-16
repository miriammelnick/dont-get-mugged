
###############################################################################
#
# GetDemographicsForNation
# Retrieve demographic information for the entire nation.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetDemographicsForNation(Choreography):

    """
    Create a new instance of the GetDemographicsForNation Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/DataGov/GetDemographicsForNation')


    def new_input_set(self):
        return GetDemographicsForNationInputSet()

    def _make_result_set(self, result, path):
        return GetDemographicsForNationResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetDemographicsForNationChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetDemographicsForNation
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetDemographicsForNationInputSet(InputSet):
        """
        Set the value of the DataVersion input for this choreography. ((optional, string) Specify the census data version to search, such as "jun2011" (the default).)
        """
        def set_DataVersion(self, value):
            InputSet._set_input(self, 'DataVersion', value)


"""
A ResultSet with methods tailored to the values returned by the GetDemographicsForNation choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetDemographicsForNationResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response returned from the API.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetDemographicsForNationChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetDemographicsForNationResultSet(response, path)
