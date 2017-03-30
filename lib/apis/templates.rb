##########################################################################
# Copyright 2016 ThoughtWorks, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
##########################################################################

module APIs
  class Templates < APIBase

    def get_template(template_name)
      get("#{template_url}/#{template_name}", {'Accept'=> 'application/vnd.go.cd.v3+json'})
    end


    def index(template)

    end

    def create(template_name)
      template = Template.new(name: "#{template_name}") do |t|
        t << Stage.new(name: 'defaultStage') do |s|
          s << Job.new(name: 'defaultJob') do |j|
            j << ExecTask.new(attributes:{command: 'ls'})
          end
        end
      end
      post("#{template_url}",template.to_json, {'Accept'=> 'application/vnd.go.cd.v3+json', 'Content-Type'=> 'application/json'})
    end

    def update(template_name, payload, etag)
      put("#{template_url}/#{template_name}",payload,{'Accept'=> 'application/vnd.go.cd.v3+json','Content-Type'=> 'application/json','If-Match'=> etag})
    end

  end
end
